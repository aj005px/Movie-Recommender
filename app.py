import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import random
'''
df = pd.read_csv('imdb_top_1000.csv')
df.columns = df.columns.str.strip()
print("Current columns:", df.columns.tolist())
df['Combined_Info'] = (
    df['Genre'].astype(str) +
    ' | IMDB: ' + df['IMDB_Rating'].astype(str) +
    ' | Meta: ' + df['Meta_score'].astype(str)
)
columns_to_drop = ['Genre', 'IMDB_Rating', 'Meta_score', 'Star3', 'Star4', 'No_of_Votes']
df.drop(columns=columns_to_drop, inplace=True)
df.to_csv('updated_file.csv', index=False)
print("Updated columns:", df.columns.tolist())
'''
df=pd.read_csv('updated_file.csv')
vectorizer =TfidfVectorizer(max_features=10000,stop_words='english')
vector = vectorizer.fit_transform(df['Combined_Info'].values.astype('U'))#converted array and unicode
random_movies=df.sample(3).reset_index()
print("Choose the following options")
for i, row in random_movies.iterrows():
   print(f"{i+1}. {row['Series_Title']}")
print("4. Enter your Movie")
choice=int(input("Enter the option"))
if choice in [1,2,3]:
    movie_idx = random_movies.loc[int(choice)-1, 'index']
elif choice==4:
    user_input=input("Enter a movie").lower()
    matches = df[df['Series_Title'].str.lower().str.contains(user_input)]
    if matches.empty:
        print("Movie not found")
        exit()

    movie_idx = matches.index[0]
else:
    print("Invalid option")
    exit()
similarities = cosine_similarity(vector[movie_idx], vector).flatten()
sorted_indices = similarities.argsort()[::-1]

count = 0
idx = 0

print("\nRecommended movies:\n")

for idx in sorted_indices:
    if idx != movie_idx and similarities[idx] > 0.1:
        print(df.iloc[idx]['Series_Title'],
              "| Score:", round(similarities[idx], 3))
        count += 1
    if count == 5:
        break
