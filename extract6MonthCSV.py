import pandas as pd
from datetime import datetime, timedelta

# Step 1: Read the CSV file
csv_file_path = 'Slack-app-reviews.csv'  # Change this to your actual CSV file path
data = pd.read_csv(csv_file_path)

# Step 2: Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Ensure dates are converted

# Step 3: Get today's date and calculate the date six months ago
today = datetime.now()
six_months_ago = today - timedelta(days=6 * 30)  # Approximate 6 months

# Step 4: Filter the DataFrame for the last six months
recent_data = data[data['date'] >= six_months_ago]

# Step 5: Sort the filtered DataFrame by date in descending order
recent_data = recent_data.sort_values(by='date', ascending=False)

# Step 6: (Optional) Save the sorted data to a new CSV file
recent_data.to_csv('recent_reviews_sorted.csv', index=False)

# Print the sorted DataFrame to verify
print(recent_data)
