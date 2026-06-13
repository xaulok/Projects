import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "tweepy", "pandas"])
import pip
import tweepy
import pandas as pd
from textblob import TextBlob
import nltk

# Twitter API credentials
consumer_key = 'VUG869XkrCg9MWcCwt6kXDsby'
consumer_secret = 'vwsrc1TZiMgoV1S2yWJ88m99mdRuCZHhgKNns4ISdL1JepkSOy'
access_token = '2058160730529284096-pbIxiH4a6C9KSMWD7qoG0AQjchQnHb'
access_token_secret = 'mnS5OsM4R4z3vuLNvfB7JMmTRpIP0ecGRJPVV4wqYI1hc'

# Connecting to Twitter API using Tweepy
bearer_token = "AAAAAAAAAAAAAAAAAAAAAON4%2BAEAAAAAwI7%2Fbm7wFx4sLcXEou5xmCVNo58%3D8O7mTyBhJMimsbMukkPJWGg39twcds4Jb3ofbMFWCTAlqF5Jvo"
client = tweepy.Client(bearer_token=bearer_token)
tweets = client.search_recent_tweets(
    query="AI lang:en -is:retweet",
    max_results=100
)
for tweet in tweets.data:
    print(tweet.text)

#store the tweets in a pandas DataFrame
df = pd.DataFrame([tweet.text for tweet in tweets.data], columns=['Tweet'])
print(df.head())

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
# Function to fetch tweets based on a keyword
def fetch_tweets(keyword, count=100):
    try:
        tweets = api.search_tweets(q=keyword, count=count, lang='en')
        return [tweet.text for tweet in tweets]
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []
# Example usage
if __name__ == "__main__":
    keyword = "Python programming"
    tweets = fetch_tweets(keyword)
    df = pd.DataFrame(tweets, columns=['Tweet'])
    print(df.head())

# Ensure required NLTK packages are installed separately
nltk.download('punkt')
nltk.download('vader_lexicon')
# clean the tweets (remove URLs, mentions, hashtags, etc.)
import re
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text
df["Clean_Tweet"] = df["Tweet"].apply(clean_text)
# Display the cleaned tweets
print(df[["Tweet", "Clean_Tweet"]].head())


# Perform sentiment analysis using VADER
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
def analyze_sentiment_vader(tweet):
    sentiment = sia.polarity_scores(tweet)
    if sentiment['compound'] > 0:
        return 'Positive'
    elif sentiment['compound'] < 0:
        return 'Negative'
    else:
        return 'Neutral'
# Apply VADER sentiment analysis to the DataFrame
df['Sentiment_VADER'] = df['Tweet'].apply(analyze_sentiment_vader)
print(df.head())


# Perform sentiment analysis using TextBlob
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'
# Apply sentiment analysis to the DataFrame
df['Sentiment'] = df['Tweet'].apply(analyze_sentiment)
print(df.head())

# Visualize the sentiment distribution
import matplotlib.pyplot as plt
sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar')
plt.title('Sentiment Distribution of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Save the DataFrame to a CSV file
df.to_csv('tweets_sentiment_analysis.csv', index=False)
# Save the DataFrame to an Excel file
df.to_excel('tweets_sentiment_analysis.xlsx', index=False)



# Building Dashboard using Streamlit
import streamlit as st
# Set up the Streamlit app
st.title("Twitter Sentiment Analysis Dashboard")
st.write("This dashboard shows the sentiment analysis of recent tweets about AI.")
# Display the sentiment distribution
st.subheader("Sentiment Distribution")
sentiment_counts = df['Sentiment'].value_counts()
st.bar_chart(sentiment_counts)
# Display the DataFrame
st.subheader("Tweets and Sentiment")
st.dataframe(df[['Tweet', 'Sentiment']])
