import sys
from bs4 import BeautifulSoup as soup

import urllib2 as url2

from testmodule.styleformat import heading

#Tag, NavigableString, BeautifulSoup, and Comment. These are the four types
#of Object that we usually deal with while parsing using beautifulsoup
heading("Module 10 Assignments: 2web scraping program to display \
         top 250 movies rated in IMDB.com. Output should be in the below format:")

'''
Seral num . Movie name (Release_year)
Ex 242. Gravity (2013)
'''
def has_class(tag):
    return tag.has_attr('class')

def parse_soup(soup_contents):
    #print soup_contents

    tbody= soup_contents.find('tbody')
    if has_class(tbody):
        print "class =  ",
        print tbody['class']
    #print tbody

    while (tbody != ''):
        if "lister-list" in tbody['class']  :
            lister_list_tbody = tbody
            break

        tbody = soup_contents.find_next('tbody')

    return parse_table_data(lister_list_tbody)

def parse_table_data(table):
    movies = list()
    for row in table.find_all('tr'):
        movie = list()
        #print "-" * 30
        for col in row.find_all('td'):
            #print "*"* 30
            #print type(col)
            #print col
            #print col['class']
            if 'titleColumn' in col['class']:
                contents = col.contents
                movie.append((contents[0]).strip())
                movie.append(contents[1].string)
                movie.append(contents[3].string)
        movies.append(movie)
    return movies

def getWebsite(argument):
    print "Fetching.. "+ (argument)
    html = url2.urlopen(argument)

    s = soup(html)
    #print s
    movies_list = parse_soup(s)

    print "Sl. Name. Year"
    for index, value in enumerate(movies_list):
        len(value)
        print  value[0],
        print  value[1],
        print  value[2]

if __name__ == "__main__":
    print "Attention: http_proxy and https_proxy env variables are properly set and reflected in pycharm"
    url_from_browser = "http://www.imdb.com/chart/top?ref_=nv_mv_250_6"
    getWebsite(url_from_browser)


