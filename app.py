import streamlit as st
import pickle
import pandas as pd
import requests


st.title('Movie Recommender')

movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity_list = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies_list['title'].values


df = pickle.load(open('movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(df)

Selected_movie_name  = st.selectbox('Which type of movie would you like to watch?', (movies_list))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6f4fb72fff652b0413524bd5e146dc33&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    

def recommend(movie):
    movie_idx = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity_list[movie_idx]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:7]
    recommended_list = []
    recommended_list_poster = []
    
    for i in movie_list:
        m_id = movies_df.iloc[i[0]].movie_id
        recommended_list.append(movies_df.iloc[i[0]].title)
        recommended_list_poster.append(fetch_poster(m_id))
        
    return recommended_list, recommended_list_poster



if st.button('Recommend'):
    name, poster = recommend(Selected_movie_name)
    col1, col2 = st.columns(2)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
        
    col3, col4 = st.columns(2)
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
        
    col5, col6 = st.columns(2)
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])
