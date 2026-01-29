import streamlit as st
st.title("My first Streamlit website!")
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name} Welcome to Streamlit!")
