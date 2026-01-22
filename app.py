import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import random

st.title("🍿 Movie Recommender")
st.subheader("Choose a movie you like:")

# Load data
df = pd.read_csv('updated_file.csv')

# Vectorize combined info
vectorizer = TfidfVectorizer(max_features=10000, stop_words='english')
vector = vectorizer.fit_transform(df['Combined_Info'].values.astype('U'))

# Show 3 random movies as clickable buttons with posters
random_movies = df.sample(3).reset_index()
st.write("Select one of the following movies:")

movie_idx = None
cols = st.columns(3)
for i, (col, row) in enumerate(zip(cols, random_movies.itertuples())):
    with col:
        st.image(row.Poster_Link, width=100)
        st.write(row.Combined_Info)
        if st.button(row.Series_Title, key=i):
            movie_idx = row.index

# Option 4: Enter your own movie
st.write("Or enter your own movie:")
user_input = st.text_input("Type movie name here:")

if movie_idx is None:
    if user_input:
        matches = df[df['Series_Title'].str.lower().str.contains(user_input.lower())]
        if matches.empty:
            st.write("Movie not found")
            st.stop()
        movie_idx = matches.index[0]
    else:
        st.stop()

# Compute similarities
similarities = cosine_similarity(vector[movie_idx], vector).flatten()
sorted_indices = similarities.argsort()[::-1]

# Display top 5 similar movies in a row
st.write("### Recommended movies:")
top_movies = []
for idx in sorted_indices:
    if idx != movie_idx and similarities[idx] > 0.1:
        top_movies.append(idx)
    if len(top_movies) == 5:
        break

cols = st.columns(len(top_movies))
for col, idx in zip(cols, top_movies):
    with col:
        st.image(df.iloc[idx]['Poster_Link'], width=100)
        st.write(
            df.iloc[idx]['Series_Title'],
            df.iloc[idx]['Combined_Info'],
            "\nLikability:", f"{round(similarities[idx]*100, 2)}%"
        )
