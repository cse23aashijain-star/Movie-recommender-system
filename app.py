import streamlit as st
import pandas as pd
import pickle
import os
import gdown
import requests

# Download similarity.pkl from Drive if not already in repo
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1Gs2G-n7X15Hn58emq-d0S-6k67ireZ4a"
    gdown.download(url, "similarity.pkl", quiet=False)

# Load similarity.pkl
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Load movies.pkl directly from repo
with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)

# --- STREAMLIT UI ---
st.title("Movie Recommender")
movie_name = st.selectbox("Select a movie:", movies_list['title'].values)
if st.button("Recommend"):
    recommendations = recommend(movie_name)
    for rec in recommendations:
        st.write(rec)

# movies_list → because it is the DataFrame
#
# movie → because that is what user selected
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    distances = similarity[movie_index]
    movie = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommended_movies =[]
    for i in movie:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies=movies_list['title'].values


st.title ('Movie Recommender System')
selected_movie_name =st.selectbox(
    'Choose a movie to recommend',
    movies)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
       st.write(i)




