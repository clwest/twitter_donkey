
# Twitter Donkey

I am working on a group of bots using the Twitter API and various other packages such as tweepy and Erin. The end project goal is to take the Twitter data and be able to bring it onto the blockchain.


Followers folder:
    The data folder contains the JSON files of projects that I am interested in and a list of people that have already been followed. I used postman to set up this file

    config.py is where you will keep all of your API keys, dotenv will not work for some reason
    follows.py scans the list of projects from the data file and randomly follows 50 new accounts.
    getuser.py does nothing exciting
Sentiment Folder:
    This folder will contain all of the files that I will be building to get the sentiment from different projects to make investment choices in defi and plan on storing it on ipfs when it's done!
    The projects in this folder will require an elevated Twitter API key.
