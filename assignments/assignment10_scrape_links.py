import sys
from bs4 import BeautifulSoup as soup

import urllib2 as url2

from testmodule.styleformat import heading

heading("Module 10 Assignments: 1 find urls from any website that you \
pass as command line argument. You may pass one or multiple \
web pages at a time")

'''
Example: You may want to execute it by:
Python your_script.py http://reddit.com http://yellowpages.com
'''
def parse_soup(soup_contents):
    all_anchor = soup_contents.find_all('a')
    all_links = list()
    for anchor in all_anchor:
        href = anchor.get('href')
        #print href
        all_links.append(href)

    # filter the local hrefs e.g /careers/?ref=pf /privacy/explanation /policies/cookies/ /policies?ref=pf
    return filter(lambda x: not x.find("http"),all_links)

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
    arguments = list()
    if len(sys.argv) >= 2:
        arguments = sys.argv[1:]
    for argument in arguments:
        print "*" * 30 + argument + "*" * 30
        getWebsite(argument)


