import tweepy

# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "bSh5wvnGDnoE0HShQjbLcDCj5"
consumer_secret = "mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
access_key = "2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
access_secret = "BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff"

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
