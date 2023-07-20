import api
import streamlit as st


st.title("NUMBER TRIVIA GENERATOR")
input_integer = st.text_input("Enter an integer number (e.g., 42): ", 42)

st.write(f"_{api.get_fact(input_integer)[0]}_")