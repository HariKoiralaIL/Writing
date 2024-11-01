import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Step 1: Read the CSV file
csv_file_path = 'Slack-app-reviews.csv'  # Change this to your actual CSV file path
data = pd.read_csv(csv_file_path)

# Step 2: Convert the date column to datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Convert and handle any errors

# Step 3: Filter for reviews from the last 6 months
six_months_ago = datetime.now() - timedelta(days=180)  # Calculate the date 6 months ago
recent_reviews = data[data['date'] >= six_months_ago]  # Filter the DataFrame

# Step 4: Check the filtered data
print(recent_reviews[['date', 'review', 'rating']].head(10))  # Display the first 10 recent reviews

# Step 5: Create a bar graph for the ratings
# Count the occurrences of each rating
rating_counts = recent_reviews['rating'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 5))
rating_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rating Distribution for the Last 6 Months')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

# Optional: Display the total number of recent reviews
print(f'Total number of reviews in the last 6 months: {recent_reviews.shape[0]}')
