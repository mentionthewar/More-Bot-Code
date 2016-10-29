
import time
import tweepy
from keys import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

user = api.me()

#Returning some example data from the api
print(user.name)
print(user.location)
print(user.followers_count)
print(user.notifications)

#grab five mentions
mentions = api.mentions_timeline(count=5)

#This is a bit messy
print(mentions)


