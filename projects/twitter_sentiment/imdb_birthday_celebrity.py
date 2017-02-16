import sys
from bs4 import BeautifulSoup as soup

import urllib2 as url2
from webpage_renderer import Render

from testmodule.styleformat import heading

#Tag, NavigableString, BeautifulSoup, and Comment. These are the four types
#of Object that we usually deal with while parsing using beautifulsoup
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
        r = Render(url)
        # result is a QString.
        result = r.frame.toHtml()
        result_py = str(result.toAscii())
        s = soup(result_py, "lxml")
        #print s

        celeb_list = BirthDayCelebrities.parse_soup(s)

        for index, celeb in enumerate(celeb_list):
            print '-' * 50 + str(index + 1) + '-' * 50
            print "Name: " + celeb[0]
            print "Image: " + celeb[1]
            print "Profession: " + celeb[2]
            print "Best works: " + celeb[3]


if __name__ == "__main__":
    print "*** Attention***: http_proxy and https_proxy env variables are properly set and reflected in pycharm"
    url_from_browser = "http://m.imdb.com/feature/bornondate"
    celeb = BirthDayCelebrities()
    BirthDayCelebrities.getDetails(url_from_browser)
