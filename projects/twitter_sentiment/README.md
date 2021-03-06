# `Problem statement: ` ``"Twitter Sentiment Analysis"``
Twitter sentiment analysis about an actor taken birth on this date as per the IMDB data.
Perform such analysis for 10 actors shown in the top of the list.

_This project was done as part of a Project evaluation task given by [Edureka](https://www.edureka.co/)_

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

__How to use this project:__
You can execute the script by `python imdb_birthday_celebrity.py
 consumer_key consumer_secret access_token access_token_secret`
 _You must aquire these keys by creating an app account in twitter._
 _They are not shared for secirity reasons._


__Additional packages installed:__
* `python-qt4`
* `tweepy 3.5.0` (API has input argument for proxy)
* `requests 2.13.0`
* `PySocks 1.6.6`
* `six 1.10.0`
* `requests-oauthlib 0.8.0`
* `oauthlib 2.0.1`
* `python-skimage 0.9.3`


__Local Contents:__ For ease, a static content has been provided in the folder `test_data`
Using the `test_data/imdb.html` the problems associated with internet can be avoided and 
one can get started quickly. To make use of local contents, please make use of `BirthDayCelebrities.getDetailsLocalContent()`
in python source file `imdb_birthday_celebrity.py` under main section.

__Sample Output:__ Sometimes having the necessary developement setup is a time consuming task.
For viewing the final output samples of this project, please take a look at `gen` [folder.](https://github.com/Kalinga/pythonLearning/tree/master/projects/twitter_sentiment/gen)

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

**Celebrity Icon quality:** The Link for the celebrity icon was of small size, and displaying
that in the pyplot was getting blurred. So I looked for a better image, that i found from desktop
website and found a pattern in the link for the smaller image and bigger image.
See below images, The links for the images differ in the last part of the links.

![Smaller Image](https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1MjQ3MjQyOF5BMl5BanBnXkFtZTcwMTYxODgwNQ@@._V1._CR1,0,1388,2048_SX40_SY59.jpg "Ron Eldard ")


![Larger Image](https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1MjQ3MjQyOF5BMl5BanBnXkFtZTcwMTYxODgwNQ@@._V1_QL50_SY1000_CR0,0,666,1000_AL_.jpg "Ron Eldard ")

__Known issues__: Few times `loadfinish` of the Webkit Page does not come, without that parsing
never get started and process halts indefinitely.

# License:
[The MIT License](LICENSE)