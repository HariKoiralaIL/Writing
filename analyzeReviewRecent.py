import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Step 1: Read the sorted recent reviews CSV file
recent_reviews_file = 'recent_reviews_sorted.csv'
data = pd.read_csv(recent_reviews_file)

# Step 2: Ensure the 'rating' column is properly formatted
data['rating'] = data['rating'].astype(str)  # Ensure ratings are strings

# Step 3: Categorize reviews by rating
low_rated_reviews = data[data['rating'].str.split('/').str[0].astype(int) <= 2]  # 1-2 stars
high_rated_reviews = data[data['rating'].str.split('/').str[0].astype(int) >= 4]  # 4-5 stars

# Step 4: Extract keywords from reviews
def get_most_common_words(reviews, top_n=10):
    vectorizer = CountVectorizer(stop_words='english')  # Exclude common English stop words
    X = vectorizer.fit_transform(reviews['review'])  # Create a document-term matrix
    words = vectorizer.get_feature_names_out()  # Get the feature names (words)
    total_counts = X.sum(axis=0).A1  # Sum the counts for each word
    word_counts = dict(zip(words, total_counts))  # Create a dictionary of word counts
    
    # Get the most common words
    most_common = Counter(word_counts).most_common(top_n)
    return most_common

# Step 5: Analyze low and high rated reviews
low_common_words = get_most_common_words(low_rated_reviews)
high_common_words = get_most_common_words(high_rated_reviews)

def plot_common_words(common_words, title):
    words, counts = zip(*common_words)  # Unzip into words and counts
    plt.figure(figsize=(10, 6))
    plt.barh(words, counts, color='skyblue')
    plt.xlabel('Count')
    plt.title(title)
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest count at the top
    plt.show()

# Plot the common words
plot_common_words(low_common_words, "Most Common Words in Low Rated Reviews")
plot_common_words(high_common_words, "Most Common Words in High Rated Reviews")
