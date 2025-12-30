import streamlit as st
import pandas as pd
import pickle

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







