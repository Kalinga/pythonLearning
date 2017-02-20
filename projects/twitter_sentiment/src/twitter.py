import os
import sys
import tweepy
from sentiment import Senti

class Twitter(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        #self.api = tweepy.API(auth)#,proxy='https://username:password@proxy.company.com:8080')

    def getTweets(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print "-" * 120
            print tweet.text
        print "-" * 120

    def getMatchedTweets(self, q, lang='', locale='', since_id='', geocode='', count=50):
        all_matched_tweets = self.api.search(q = q, count = count)
        all_matched_tweet_text = "\n".join(map(lambda x: x.text, all_matched_tweets))

        # for tweet in all_matched_tweets:
        #     print "-" * 120
        #     print tweet.text
        # print "-" * 120

        return all_matched_tweet_text


if __name__ == "__main__":
    #print sys.argv
    twitter = Twitter(*sys.argv[1:])
    #twitter.getTweets()

    celeb = 'Trump'
    celeb_tweets = twitter.getMatchedTweets(q = celeb, lang='en', count=1000)
    #print celeb_tweets

    file_name = 'tweet_' + celeb + '.txt'
    write_file_name = os.path.join(os.getcwd(), "gen", file_name)

    with open(write_file_name, 'w') as file_write:
        file_write.write(celeb_tweets.encode("utf-8"))

    senti = Senti()
    senti.sentiment_analysis(write_file_name, celeb)