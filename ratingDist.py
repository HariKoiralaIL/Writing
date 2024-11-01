import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Slack-app-reviews.csv')

if df['rating'].dtype == object:
    df['rating'] = df['rating'].str.split('/').str[0].astype(float)
else:
    df['rating'] = df['rating'].astype(float)

df = df.dropna(subset=['rating'])

# Plot a histogram of the ratings
plt.figure(figsize=(8,6))
df['rating'].hist(bins=5, edgecolor='black')
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.grid(False)
plt.show()
