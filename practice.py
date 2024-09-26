import streamlit as st

st.title("My First Streamlit App")
st.write("This is a simple Streamlit app.")

user_input = st.text_input("Enter your name.")
st.write("Your name is", user_input)

age = st.slider("Choose your age", 1, 100)
st.write("You are", age, " years old")

if st.button('Say hello'):
  st.write("Hello there.")

