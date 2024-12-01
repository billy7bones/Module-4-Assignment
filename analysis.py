import pandas as pd

# File path
file_path = r"H:\My Drive\Nexford\MSc Business Analytics\Programming in R & Python - BAN6420\Module 4- Data Visualization in R and Python for Data Analysis\Module 4 Assignment\Netflix_shows_movies.csv"

# Load the dataset
try:
    netflix_data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the path.")
# Check for missing values
print("Missing values before cleaning:\n", netflix_data.isnull().sum())

# Fill missing values
# Replace missing genres with "Unknown"
if 'genre' in netflix_data.columns:
    netflix_data['genre'] = netflix_data['genre'].fillna("Unknown")

# Replace missing ratings with the mode
if 'rating' in netflix_data.columns:
    netflix_data['rating'] = netflix_data['rating'].fillna(netflix_data['rating'].mode()[0])

# Drop rows with missing critical information (e.g., title)
if 'title' in netflix_data.columns:
    netflix_data.dropna(subset=['title'], inplace=True)

# Confirm cleaning
print("Missing values after cleaning:\n", netflix_data.isnull().sum())
# Display dataset summary
print("Dataset Summary:")
print(netflix_data.info())

# Display basic statistics
print("Basic Statistics:")
print(netflix_data.describe(include='all'))

# Display unique values in key columns
if 'genre' in netflix_data.columns:
    print("Unique Genres:", netflix_data['genre'].unique())
if 'rating' in netflix_data.columns:
    print("Unique Ratings:", netflix_data['rating'].unique())
# Check if 'genre' column exists and has data
if 'genre' in netflix_data.columns:
    print("Genre column exists.")
    print(netflix_data['genre'].head())
else:
    print("Genre column not found.")
# Print column names
print("Available columns:", netflix_data.columns)
import seaborn as sns
import matplotlib.pyplot as plt

# Most Watched Genres (from listed_in column)
if 'listed_in' in netflix_data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=netflix_data,
        y='listed_in',
        order=netflix_data['listed_in'].value_counts().index,
        palette="viridis"
    )
    plt.title("Most Watched Genres", fontsize=16)
    plt.xlabel("Count")
    plt.ylabel("Genres")
    plt.tight_layout()
    plt.show()
else:
    print("'listed_in' column not found. Cannot create plot.")
# Display unique values in the 'listed_in' column
print("Unique Genres (listed_in):", netflix_data['listed_in'].unique())
from collections import Counter

# Split the 'listed_in' column into individual genres
genre_counts = Counter(
    genre.strip() for genres in netflix_data['listed_in'].dropna() for genre in genres.split(",")
)

# Convert to a DataFrame for easier plotting
genre_df = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

# Bar plot for individual genres
plt.figure(figsize=(10, 6))
sns.barplot(data=genre_df, y='Genre', x='Count', palette="viridis")
plt.title("Most Watched Genres (Individual)", fontsize=16)
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
