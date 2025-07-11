import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'));
st.title('Movie Recommender System');

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
