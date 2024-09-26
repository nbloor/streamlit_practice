import streamlit as st

st.title("My First Streamlit App")
st.write("This is a simple Streamlit app.")

user_input = st.text_input("Enter your name.")
st.write("Your name is", user_input)
