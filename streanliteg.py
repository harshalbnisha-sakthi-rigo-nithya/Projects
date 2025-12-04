import streamlit as st

st.title('My First Streamlit App')
st.header('Demo app')
st.write("This is a simple a app created with Streamlit")

name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age", 1,100,25)
st.write(f"You selected: {age}")