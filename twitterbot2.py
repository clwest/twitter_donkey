import tweepy
from dotenv import load_dotenv
load_dotenv()
import os
import json


twitter_api = os.environ.get("TWITTER_API")
twitter_secret = os.environ.get("TWITTER_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


def getClient():
    client = tweepy.Client(bearer_token, twitter_api, twitter_secret, client_id, client_secret)
    return client

def getUserInfo():
    client = getClient()
    user = client.get_user(username="jack")
    return user.data

user = getUserInfo()
print(user)

def searchTweets(client, query, max_results=10):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    tweets_data = tweets.data 
    results = []
    
    if not tweet_data is None and len(tweets_data) > 0:
        for tweet in tweets_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj)
    return results



def getTweet(client, id):
    tweet = client.get_tweet(id, expansion=['author_id'], user_fields=['username'])
    return tweet

def returnSearchTweetList(query, max_results=10):
    client = getClient()
    tweets = searchTweets(client, query, max_results)
    
    objs = []
    if len(tweets) > 0:
        for tweet in tweets:
            twt = getTweet(client, tweet['id'])
            obj = {}
            obj['text'] = tweet['text']
            obj['username'] = twt.includes['users'][0].username
            obj['id'] = tweet['id']
            obj['url'] = 'https://twitter.com/{}'.format(twt.includes['users'][0].username, tweet['id'])
            objs.append(obj)
    return objs

def retweet(id):
    client = getClient()
    client.retweet(id)
    
