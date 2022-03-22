import requests
import tweepy
import os
import json
from dotenv import load_dotenv
from csv import writer
load_dotenv()
import os
import pandas as pd

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get("BEARER_TOKEN")
twitter_api = os.environ.get("TWITTER_API")
twitter_secret = os.environ.get("TWITTER_SECRET")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth = tweepy.OAuthHandler(twitter_api, twitter_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# tweets from users account

user = 'donkeybetzking'
limit = 300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# for tweet in tweets:
#     print(tweet.full_text)
    
# create dataframe
columns = ["User", "Tweet"]
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
    
df = pd.DataFrame(data, columns=columns)

print(df)