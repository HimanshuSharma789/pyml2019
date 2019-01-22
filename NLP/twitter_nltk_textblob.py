import sys
import string
import matplotlib.pyplot as plt
import nltk
import tweepy
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
tweets = api.search(sys.argv[1], count=10, lang='en')
# tweets = tweepy.Cursor(api.search, q=sys.argv[1], lang='en').items(10)

data = ""
for tweet in tweets:
    data = data + "\n" + tweet.text
    print(tweet.text)

with open("twitter_tweets_data.txt", "w", encoding="utf-8") as file:
    file.write(data)

polar = []
for tweet in tweets:
    analyze = TextBlob(tweet.text)
    check = analyze.sentiment.polarity
    polar.append(check)

plt.plot(range(len(tweets)), polar, marker='o')
plt.title("Polarity")
plt.show()
print("@@@@@@@@@@@@-------polarity--------------@@@@@@@@@@@@@")

sent_token = sent_tokenize(data)
stem1 = PorterStemmer()

for i in range(len(sent_token)):
    words = word_tokenize(sent_token[i])
    new_word = [stem1.stem(word) for word in words]
    sent_token[i] = " ".join(new_word)

sentence = sent_token
print(sentence)
print("@@@@@@@@@@@@-------token--------------@@@@@@@@@@@@@")
for j in range(len(sentence)):
    words1 = word_tokenize(sentence[j])
    new_word1 = [word for word in words1 if word not in stopwords.words('english') and word not in string.punctuation]
    sentence[j] = " ".join(new_word1)
print(sentence)
print("@@@@@@@@@@@@--------stopwords-------------@@@@@@@@@@@@@")

sentence = " ".join(sentence).split()
print("@#@#@#@#@#@\n ")
print(sentence)
freq_dist = nltk.FreqDist(sentence)
print(freq_dist.plot())
top_words = freq_dist.most_common(10)
print(top_words)
plt.bar(range(10), list(dict(top_words).values()))
plt.xticks(range(10), list(dict(top_words).keys()))
plt.title("Word Occurrence")
plt.show()

