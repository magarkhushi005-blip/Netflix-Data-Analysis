import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
df = pd.read_csv("Data/netflix1.csv")

# Display the first 5 rows
print(df.head())

# Display dataset information
print(df.info())


# Check dataset shape
print("Shape of dataset:", df.shape)

# Check column names
print("Columns:")
print(df.columns)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df['director'] = df['director'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Not Rated")
df['duration'] = df['duration'].fillna("Unknown")

# Remove rows where date_added is missing
df = df.dropna(subset=['date_added'])

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Create new columns
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_netflix.csv", index=False)

print("\nData cleaning completed successfully!")

plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar', color=['skyblue', 'orange'])
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar', color='green')
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(data=df, y='country', order=df['country'].value_counts().index[:10])
plt.title("Top 10 Countries")
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Split multiple genres into separate rows
genre = df['listed_in'].str.split(', ').explode()

# Count top 10 genres
top_genres = genre.value_counts().head(10)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genres")

plt.show()

# Country Analysis

country = df['country'].str.split(', ').explode()

top_countries = country.value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index)

plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()
plt.figure(figsize=(10,5))
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

import matplotlib.pyplot as plt

# Count Movies and TV Shows
type_count = df['type'].value_counts()
# Create Pie Chart
 
plt.figure(figsize=(7,7))

plt.pie(
    type_count,
    labels=type_count.index,
    autopct='%1.1f%%',
    startangle=90,
    explode=(0.05, 0.05),
    shadow=True
)

plt.title("Movies and TV Shows on Netflix")
plt.title("Distribution of Movies and TV Shows on Netflix")
plt.savefig("movies_vs_tvshows_piechart.png")
plt.show()
