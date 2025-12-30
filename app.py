import streamlit as st
import pandas as pd
import pickle
import os
import requests

# --- DOWNLOAD SIMILARITY FILE IF NOT PRESENT ---
file_path = "similarity.pkl"
if not os.path.exists(file_path):
    url = "https://drive.google.com/uc?export=download&id=1Gs2G-n7X15Hn58emq-d0S-6k67ireZ4a"
    print("Downloading similarity.pkl ...")
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download complete!")

# --- LOAD DATA ---
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))

# --- RECOMMEND FUNCTION ---
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list_sorted:
        movie_id = i[0]
        # fetch poster from API if needed
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

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



