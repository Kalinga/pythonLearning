#Problem statement: "Twitter Sentiment Analysis"
Twitter sentiment analysis about an actor taken birth on this date as per the IMDB data.
Perform such analysis for 10 actors shown in the top of the list.

__Details:__
IMDB provides a list of celebrities born on the current date. Below is the link:
[IMDB](http://m.imdb.com/feature/bornondate).
List of celebrity from this webpage can be obtained using web scraping
(the ones that are displayed i.e. top 10). Below information can be extracted:
> * Name of the celebrity
> * Celebrity Image
> * Profession
> * Best Work

Sentiment analysis on twitter for each celebrity should be run and the expected output
will be in the below format.
> * Name of the celebrity:
> * Celebrity Image:
> * Profession:
> * Best Work:
> * Overall Sentiment on Twitter: Positive, Negative or Neutral:

 
 __Problem Faced:__
 _url2.urlopen_ just give the static html contents where the JavaScript name is present,
 however we need the rendered contents/final content, that we need for our purpose.
 Many solutions to this problem exists, and found on searching the internet.
 * Solution 1: Using `PyQt4.QtGui, PyQt4.QtCore, PyQt4.QtWebKit`
 * Solution 2: Using `dryscrape`
 * Solution 3: Using `selenium.webdriver`
   
Initially, I thought to make use of _'dryscrape'_, thinking others will take more time.
However, after looking _'dryscrape'_ documentation, i changed my mind and used
first solution(because when i checked my system, i had 'python-qt4' was already installed ).

__Additional packages installed:__
* `python-tweepy`
* `python-oauth`

