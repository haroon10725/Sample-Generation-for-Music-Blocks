import streamlit as st
from main import generate_music

st.header("Sample Generation for Music Blocks")

prompt = st.text_input("Enter prompt:")

submit = st.button("Submit")

if submit:
    with st.spinner('Generating'):
        generate_music(prompt)
    st.audio("./sample.wav", format="audio/mpeg", loop=False)
