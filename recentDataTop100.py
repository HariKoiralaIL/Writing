import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
csv_file_path = 'Slack-app-reviews.csv'  # Change this to your actual CSV file path
data = pd.read_csv(csv_file_path)

# Step 2: Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Convert to datetime, coerce errors to NaT

# Step 3: Sort by date and get the most recent 100 reviews
recent_reviews = data.sort_values(by='date', ascending=False).head(100)

# Step 4: Count occurrences of each rating
rating_counts = recent_reviews['rating'].value_counts().sort_index()

# Step 5: Create a bar graph for the ratings
plt.figure(figsize=(10, 5))
rating_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribution of Ratings for the Most Recent 100 Reviews')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.grid(axis='y', alpha=0.75)
plt.show()
