import tweepy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

consumer_key = "bSh5wvnGDnoE0HShQjbLcDCj5"
consumer_secret = "mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
access_key = "2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
access_secret = "BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

usr_input = input()
search = tweepy.Cursor(api.search, q=usr_input, lang='en').items(10)

data = ""
for item in search:
    data = data + item.text
    # sent_token = sent_tokenize(item.text)
    # word_token = word_tokenize(item.text)
    # print(sent_token + "\n" + word_token)
    # print("\n\n")
    # print("Username: " + item.user.name)
    # print(item.text + "\n")

sent_token = sent_tokenize(data)
word_token = word_tokenize(data)
print(sent_token, word_token)
print("\n\n")

text = nltk.Text(word_token)
print(text)
freq_dist = nltk.FreqDist(text)
print(freq_dist)
print(freq_dist.plot())
