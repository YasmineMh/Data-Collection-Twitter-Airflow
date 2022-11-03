import tweepy
import pandas as pd
import os
import json
import re
import emoji


def read_secrets() -> dict:
    filename = os.path.join("secrets.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


def extract_emojis(text: str) -> list:
    return [char for char in text if emoji.is_emoji(char)]


def run_main_etl():
    secrets = read_secrets()

    access_key = secrets["API_KEY"]
    access_secret = secrets["API_KEY_SECRET"]
    access_token = secrets["ACCESS_TOKEN"]
    access_token_secret = secrets["ACCESS_TOKEN_SECRET"]
    bearer_token = secrets["BEARER_TOKEN"]

    output_directory = secrets["OUTPUT_PATH"]

    # Twitter authentication
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=access_key,
        consumer_secret=access_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    query = "nlp"
    tweets = client.search_recent_tweets(query=query, max_results=100)

    # Extract tweets, hashtags, mentions, links and emojis
    refined_tweets = []
    for tweet in tweets.data:
        raw_tweet = tweet.text
        tags = re.findall("#([a-zA-Z0-9_]{1,50})", raw_tweet)
        mentions = re.findall("@([a-zA-Z0-9_]{1,50})", raw_tweet)
        urls = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            raw_tweet,
        )
        emojis = extract_emojis(raw_tweet)

        refined_tweet = {
            "raw_tweet": raw_tweet,
            "hashtags": tags,
            "mentions": mentions,
            "urls": urls,
            "emojis": emojis,
        }

        refined_tweets.append(refined_tweet)

    # Save the dataframe to a csv file
    df = pd.DataFrame(refined_tweets)
    df.to_csv(output_directory + "refined_tweets.csv")
