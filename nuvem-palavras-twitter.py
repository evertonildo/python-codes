# Importing packages
import tweepy as tw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
from os import path
import random
from scipy.ndimage import gaussian_gradient_magnitude
import os
from dotenv import load_dotenv
load_dotenv()
# openai.api_key = os.environ["API_SECRET_KEY"]


# Updating credentials
consumer_key = os.environ["CONSUMER_TWITTER_API_KEY"]
consumer_secret = os.environ["CONSUMER_TWITTER_API_SECRET_KEY"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# seting variables for search
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Testing with a small set of data
query = "Athletico" + " -filter:retweets"
tweets = tw.Cursor(api.search,
                       q=query).items(10)
for tweet in tweets:
  print(tweet.text)
  
