import streamlit as st
import pickle
import urllib
# import numpy as np
# import pandas as pd
# import requests
import webbrowser

anime = pickle.load(open('anime.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))

anime_list_toshow = anime['title'].values

st.title('Anime Recommender System')
selected_anime_name = st.selectbox('Enter Anime', anime_list_toshow)


def recommend(anime_rec):
    anime_rec_index = anime[anime.title == anime_rec].index[0]
    distance = similarity[anime_rec_index]
    recc_anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_anime = []
    recommended_anime_poster = []
    recommended_anime_link = []

    for i in recc_anime_list:
        recommended_anime.append(anime.iloc[i[0]].title)
        recommended_anime_poster.append(anime.iloc[i[0]].img_url)
        recommended_anime_link.append(anime.iloc[i[0]].link)
    return recommended_anime, recommended_anime_poster, recommended_anime_link


if st.button('Recommend'):
    names, poster, anime_link = recommend(selected_anime_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(poster[0])
        if st.button(names[0]):
            webbrowser.open_new_tab(anime_link[0])
    with col2:
        st.image(poster[1])
        if st.button(names[1]):
            webbrowser.open_new_tab(anime_link[1])
    with col3:
        st.image(poster[2])
        if st.button(names[2]):
            webbrowser.open_new_tab(anime_link[2])
    with col4:
        st.image(poster[3])
        if st.button(names[3]):
            webbrowser.open_new_tab(anime_link[3])
    with col5:
        st.image(poster[4])
        if st.button(names[4]):
            webbrowser.open_new_tab(anime_link[4])

print(anime)
