import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Authorization to consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Access to user's access key and access secret
auth.set_access_token(access_key, access_secret)

# Calling api
api = tweepy.API(auth)
user = input()
search = tweepy.Cursor(api.search, q=user, lang="en").items(5)
for item in search:
    print("Username: " + item.user.name)
    print(item.text)
    print("\n")
