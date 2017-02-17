import sys
import tweepy

class Twitter(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)#,proxy='https://username:password@proxy.company.com:8080')

    def getTweets(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print "-" * 120
            print tweet.text
        print "-" * 120

    def getMatchedTweets(self, q, lang='', locale='', since_id='', geocode=''):
        all_matched_tweets = self.api.search(q = q)
        for tweet in all_matched_tweets:
            print "-" * 120
            print tweet.text
        print "-" * 120


if __name__ == "__main__":
    print sys.argv
    twitter = Twitter(*sys.argv[1:])
    twitter.getTweets()