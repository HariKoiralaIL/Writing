import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Step 1: Read the CSV file
csv_file_path = 'Slack-app-reviews.csv'  # Change this to your actual CSV file path
data = pd.read_csv(csv_file_path)

# Step 2: Extract review text
# Ensure reviews are in string format and handle any NaN values
data['review'] = data['review'].astype(str).fillna('')  # Fill NaN with empty strings

# Step 3: Perform Sentiment Analysis
def get_sentiment(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity  # Returns a polarity score between -1 (negative) and 1 (positive)

def classify_sentiment(score):
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to each review and store in 'sentiment' column
data['sentiment'] = data['review'].apply(get_sentiment)

# Create sentiment labels based on sentiment scores
data['sentiment_label'] = data['sentiment'].apply(classify_sentiment)

# Step 4: Visualize Results

# Histogram for sentiment scores
plt.figure(figsize=(10, 5))
plt.hist(data['sentiment'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Number of Reviews')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Bar chart for sentiment labels
sentiment_counts = data['sentiment_label'].value_counts()

plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Sentiment Analysis of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)  # Rotate x labels for better readability
plt.grid(axis='y', alpha=0.75)
plt.show()

# Optional: Display sentiment analysis results
print(data[['review', 'sentiment', 'sentiment_label']].head(10))  # Display the first 10 rows
print(data['sentiment_label'].value_counts())  # Count of each sentiment label

data['date'] = pd.to_datetime(data['date'])  # Ensure date column is in datetime format
data.set_index('date', inplace=True)
sentiment_trend = data.resample('M')['sentiment'].mean()  # Monthly average sentiment

plt.figure(figsize=(10, 5))
plt.plot(sentiment_trend, marker='o', linestyle='-')
plt.title('Average Sentiment Score Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score')
plt.grid()
plt.show()