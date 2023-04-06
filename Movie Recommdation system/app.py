# IMPORTING SOME IMPORTANT LIBRARIES
import streamlit as st
import pickle
import pandas as pd
import requests


# opening movies_dict.pkl file
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

# storing movies_dict data in movies object
movies  = pd.DataFrame(movies_dict)

# opening similarity.pkl file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# creating a function for fetching the poster from API of TMDB
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data_of_API = response.json()
    poster_path = data_of_API['poster_path']
    full_poster_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_poster_path

# creating a function for recommend 5 similar movies
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]  #extracting only those movie which name is matched with 'original_title'
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = list()               # empty list for storing recommended movies
    recommended_movies_posters = list()       # empty lit for storing poster of recommended movies
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id                              # extracting 'id' column from movies dataset
        recommended_movies.append(movies.iloc[i[0]].original_title)  # appending movies title
        recommended_movies_posters.append(fetch_poster(movie_id))    # appending movies poster
    return recommended_movies, recommended_movies_posters

# Giving Title for the web application
st.title('Movie Recommeder System')
# for take input from user through scrolling
selected_movie_name = st.selectbox('Please select any movie',(movies['original_title'].values))

# creating a button to get recommended movies names with poster
if st.button('Recommended'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.subheader(names[0])
    with col2:
        st.image(posters[1])
        st.subheader(names[1])
    with col3:
        st.image(posters[2])
        st.subheader(names[2])
    with col4:
        st.image(posters[3])
        st.subheader(names[3])
    with col5:
        st.image(posters[4])
        st.subheader(names[4])

