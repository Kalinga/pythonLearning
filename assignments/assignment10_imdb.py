import sys
from bs4 import BeautifulSoup as soup

import urllib2 as url2

from testmodule.styleformat import heading

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
        print "class value: ",
        print tbody['class']
    #print tbody

    while (tbody != ''):
        if "lister-list" in tbody['class']  :
            lister_list_tbody = tbody
            break

        tbody = soup_contents.find_next('tbody')

    return parse_table_data(tbody)

def parse_table_data(tbody):
    pass

def getWebsite(argument):
    print "Fetching.. "+ (argument)
    html = url2.urlopen(argument)
    s = soup(html)
    #print s
    links = parse_soup(s)
    for index, value in enumerate(links):
        print "Link " + str(index + 1) + ": " + value

if __name__ == "__main__":
    print "http_proxy and https_proxy env variables are properly set and reflected in pycharm"
    url_from_browser = "http://www.imdb.com/chart/top?ref_=nv_mv_250_6"
    getWebsite(url_from_browser)


