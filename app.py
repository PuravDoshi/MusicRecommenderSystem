import streamlit as st
import pickle
import pandas as pd

music_dict=pickle.load(open(r'/Users/puravdoshi/Downloads/MusicRecommenderSystem/music.pkl','rb'))
similarity=pickle.load(open(r'/Users/puravdoshi/Downloads/MusicRecommenderSystem/similarity.pkl','rb'))
music=pd.DataFrame(music_dict)

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music_names = []
    for i in distances:
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names

st.title('Music Recommender System')

option=st.selectbox("What music do you want to listen to ?",music['song'].values)

if(st.button("Recommend")):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)