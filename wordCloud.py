import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
csv_file_path = 'Slack-app-reviews.csv'  # Change this to your actual CSV file path
data = pd.read_csv(csv_file_path)

# Step 2: Extract review text
# The review column in your CSV is named 'review'
reviews = ' '.join(data['review'].astype(str))

# Step 3: Generate the Word Cloud
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    max_words=200,
    collocations=False  # Set to False to avoid combining words like "word1 word2"
).generate(reviews)

# Step 4: Visualize the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove axes
plt.title('Most Frequent Words in Reviews')
plt.show()
