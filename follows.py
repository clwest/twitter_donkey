import tweepy
import json
import random
import time
import config




def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)
    
def writeJson(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def getClient():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN, consumer_key=config.TWITTER_API, consumer_secret=config.TWITTER_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)
    return client

def followPeople():
    following_path = '{}data/following.json'.format(config.JSON_DIRECTORY)
    following = readJson(following_path)
    
    to_follow_path = '{}data/tofollow.json'.format(config.JSON_DIRECTORY)
    to_follow = readJson(to_follow_path)
    
    account = random.choice(to_follow)
    accountId = account['userId']
    
    client = getClient()
    
    results = client.get_users_followers(id=accountId, max_results=50)
    
    account_followers = results.data
    if len(account_followers) > 0:
        for x in account_followers:
            if not x.id in following:
                try:
                    client.follow_user(x.id)
                    following.append(x.id)
                    print('Successfully followed: {}'.format(x.username))
                    time.sleep(15)
                except:
                    print('Trouble following {}'.format(x.username))
            else:
                print('Already following {}'.format(x.username))
    writeJson(following_path, following)


followPeople()