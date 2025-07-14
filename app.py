import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))  # This should be a DataFrame
movies_df = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[index]
    movie_df = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_df:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

# UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.header("🎬 Movie Recommender System", divider="red")

# Movie dropdown
selected_movie = st.selectbox(
    "Please enter your favourite movie name",
    movies_df['title'].values
)

# Recommend button
if st.button("Recommend", type="secondary"):
    recommendations = recommend(selected_movie)
    st.subheader("You may also like:")
    for movie in recommendations:
        st.write("👉", movie)
