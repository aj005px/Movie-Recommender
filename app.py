import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
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
print(df.columns.tolist())
