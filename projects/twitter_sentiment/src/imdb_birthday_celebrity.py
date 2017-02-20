import sys
import os
from bs4 import BeautifulSoup as soup

from webpage_renderer import Render

from testmodule.styleformat import heading
from sentiment import Senti

#Tag, NavigableString, BeautifulSoup, and Comment. These are the four types
#of object that we usually deal with while parsing using beautifulsoup
heading("Class for fetching the details of birthday celebrities")
class BirthDayCelebrities(object):

    @staticmethod
    def has_class(tag):
        return tag.has_attr('class')

    @staticmethod
    def parse_table_data(table):
        celebrities = list()
        all_celeb = table.find_all('a', 'poster')
        print "Total no of celebrity: ", len(all_celeb)
        for celeb in all_celeb:
            celebrity = list()

            celebrity.append(celeb.find('div', 'label').find('span', 'title').string) #Name
            celebrity.append(celeb.find('img')['src']) #Image
            celebrity.append(celeb.find('div', 'detail').contents[0].split()[0][:-1]) #Profession
            celebrity.append(celeb.find('div', 'detail').contents[0].split(',')[1]) #Best Work
            #print celebrity
            celebrities.append(celebrity)


        return celebrities

    @staticmethod
    def parse_soup(soup_contents):
        #print soup_contents

        section = soup_contents.find('section')
        if BirthDayCelebrities.has_class(section):
            print "class =  ",
            print section['class']

            if "posters" in section['class']  :
                return BirthDayCelebrities.parse_table_data(section)
            else:
                print "HTML format for the IMDB has been changed, take a re-look"
                exit(1)


    @staticmethod
    def getDetails(url):
        print "Waiting for url to be fetched completely..."
        r = Render(url)
        print "url fetched completely..."
        # result is a QString.
        result = r.frame.toHtml()
        result_py = str(result.toAscii())
        s = soup(result_py, "lxml")
        print s

        return  BirthDayCelebrities.parse_soup(s)

    @staticmethod
    def getDetailsLocalContent():
        local_imdb = os.path.join(os.getcwd(), "test_data/imdb.html")
        with open(local_imdb, 'r') as local_file:
            html_contnet = local_file.read()
        s = soup(html_contnet, "lxml")
        print s

        return  BirthDayCelebrities.parse_soup(s)

if __name__ == "__main__":
    print "*** Attention***: http_proxy and https_proxy env variables are properly set and reflected in pycharm"
    url_from_browser = "http://m.imdb.com/feature/bornondate"

    celeb_list = BirthDayCelebrities.getDetails(url_from_browser)
    #celeb_list = BirthDayCelebrities.getDetailsLocalContent()
    #celeb_list = celeb_list[0:5]

    from twitter import Twitter
    twitter = Twitter(*sys.argv[1:])
    #twitter.getTweets()

    for index, celeb in enumerate(celeb_list):
        print '@' * 50 + str(index + 1) + '@' * 50
        print "Name: " + celeb[0]
        print "Image: " + celeb[1]
        print "Profession: " + celeb[2]
        print "Best works: " + celeb[3]

        file_name = "tweet_" + celeb[0] + ".txt"
        write_file_name = os.path.join(os.getcwd(),"gen", file_name)
        celeb_tweets = twitter.getMatchedTweets(q=celeb[0], lang='en', count=1000)

        #print celeb_tweets
        #print type(celeb_tweets)

        with open(write_file_name, 'w') as file_write:
            file_write.write(celeb_tweets.encode("utf-8"))

        senti = Senti()
        senti.sentiment_analysis(write_file_name, celeb[0], celeb[1])