import matplotlib.pyplot as plt
from skimage import io
import os
from string import punctuation
import csv
import codecs
import re

class Senti():
    def __init__(self):
        pass

    def sentiment_analysis(self, tweet_file, indiv, icon_url):
        self.tweet_file = tweet_file
        self.indiv = indiv
        pos_sent = open("positive_words.txt").read()
        positive_words = pos_sent.split('\n')
        positive_counts = []
        neg_sent = open('negative_words.txt').read()
        negative_words = neg_sent.split('\n')
        negative_counts = []
        conclusion = []

        tot_pos = 0
        tot_neu = 0
        tot_neg = 0
        all_total = 0

        #print "tweet_file", self.tweet_file
        tweets = codecs.open(self.tweet_file, 'r', "utf-8").read()
        tweet_list_dup = []

        tweets_list = tweets.split('\n')
        #print tweets_list

        for tweet in tweets_list:
            positive_counter = 0
            negative_counter = 0
            tweet = tweet.encode("utf-8")
            tweet_list_dup.append(tweet)
            tweet_processed = tweet.lower()

            # Remove punctuations
            for p in list(punctuation):
                tweet_processed = tweet_processed.replace(p, '')

            words = tweet_processed.split(' ')
            word_count = len(words)
            for word in words:
                if word in positive_words:
                    positive_counter = positive_counter + 1
                elif word in negative_words:
                    negative_counter = negative_counter + 1

            positive_counts.append(positive_counter)
            negative_counts.append(negative_counter)

            if positive_counter > negative_counter:
                conclusion.append("Positive")
                tot_pos += 1
            elif positive_counter == negative_counter:
                conclusion.append("Neutral")
                tot_neu += 0.5
            else:
                conclusion.append("Negative")
                tot_neg +=1

        #print len(positive_counts)
        output = zip(tweet_list_dup, positive_counts, negative_counts,conclusion)
        #output = output.encode('utf-8')

        print "******** Overall Analysis **************"


        if tot_pos > tot_neg and tot_pos > tot_neu:
            print "Overall Sentiment - Positive"
        elif tot_neg > tot_pos and tot_neg > tot_neu:
            print "Overall Sentiment - Negative"
        elif tot_neg == tot_neu and tot_neg > tot_pos:
            print "Overall Sentiment - Negative"
        elif tot_pos > tot_neg and tot_pos < tot_neu:
            print "Overall Sentiment - Semi Positive "
        else:
            print "Overall Sentiment - Neutral"


        print "%%%%%%%%%%%% End of stream - " + indiv + "   %%%%%%%%%%%%%%%%%%%%%"
        file_name = "tweet_sentiment_" + indiv + ".csv"
        file1 = os.path.join(os.getcwd(), "gen", file_name)

        writer = csv.writer(open(file1, 'wb'))
        writer.writerows(output)

        labels = ['Positive', '             Negative', 'Neutral']
        colors = ['yellowgreen', 'lightcoral', 'gold']

        all_total = 0
        sentiments = {}
        sentiments["Positive"] = tot_pos
        sentiments["Negative"] = tot_neg
        sentiments["Neutral"] = tot_neu
        all_total = tot_pos + tot_neg + tot_neu
        sizes = []

        sizes = [sentiments['Positive'] / float(all_total), sentiments['Negative'] / float(all_total),
                 sentiments['Neutral'] / float(all_total)]

        pattern = re.compile("(.)*_V1")
        quality_pic_pattern = "_QL50_SY1000_CR0,0,666,1000_AL_.jpg"
        icon_url = re.match(pattern, icon_url).group() + quality_pic_pattern
        #print icon_url
        image = io.imread(icon_url)

        fig1 = plt.figure() # create a figure with the default size
        ax1 = fig1.add_subplot(2,2,1)

        ax1.imshow(image, aspect='equal')
        ax1.axes.get_xaxis().set_visible(False)
        ax1.axes.get_yaxis().set_visible(False)

        plt.subplot(2,2,2)
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
        plt.axis('equal')
        plt.title('sentiment for - ' + indiv)

        file_name = "fig_" + indiv + ".png"
        fig_name = os.path.join(os.getcwd(), "gen", file_name)

        # Save the figures
        plt.savefig(fig_name)
        #plt.close()
        plt.show()