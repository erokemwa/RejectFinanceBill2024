!pip install --upgrade tweepy # upgrade to the latest version

import tweepy
import re
from collections import Counter

def authenticate_twitter(api_key, api_key_secret, access_token, access_token_secret):
    # Create OAuth1UserHandler instead of OAuthHandler
    # and pass all 4 keys directly to it
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
    # Pass the authentication handler's bearer_token to the Client constructor
    client = tweepy.Client(bearer_token=auth.access_token, wait_on_rate_limit=True)
    return client

def search_tweets(client, query, count=100):
    try:
        # Search for recent tweets
        tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=count)

        # Check if there's data before proceeding
        if tweets.data:
            return [tweet.data['text'] for tweet in tweets.data]
        else:
            print("No tweets found for your query.")
            return [] # Return an empty list if no tweets are found

    except tweepy.errors.TweepyException as e:
        print(f"Error searching for tweets: {e}")
        return [] # Return an empty list in case of an error

def extract_tweets(tweets):
    # Regex for identifying Activism (e.g., #RejectFinanceBill, #RutoMustGo)
    ticker_regex = r"\$[A-Za-z0-9]+"
    # Regex for general coin mentions
    name_regex = r"(Reject|RutoMustGo|OccupyParliament|Genz|Baddie|Teargas|Asalimiwe|Tuesday|Thursday|Resign|Sanitary Towels)"
    chant = []
    for tweet in tweets:
        # Extract tickers
        tickers = re.findall(ticker_regex, tweet)
        # Extract chant words
        names = re.findall(name_regex, tweet, re.IGNORECASE)
        chant.extend(tickers + names)
    return chant

# Replace with your Twitter API credentials
api_key = "YOUR_API_KEY"
api_key_secret = "YOUR_API_KEY_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
client = authenticate_twitter(api_key, api_key_secret, access_token, access_token_secret) # Use client variable

# Search for tweets about RejectFinanceBill2024
query = "#RejectFinanceBill2024"
tweets = search_tweets(client, query) # Pass client to search_tweets

# Extract chant word
tweets = extract_tweets(tweets)

# Count the frequency of each tweet
tweets_counts = Counter(tweets)

# Print the top 10 most mentioned chant
for tweets, count in tweets_counts.most_common(10):
    print(f"{tweets}: {count}")
