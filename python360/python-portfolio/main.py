import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title('Taiwo Akinnusoye')
    content = """Hi, I'm Taiwo. I am a full stack software engineer. 
    You'll find stuff I have worked on or working on in Python here."""
    st.info(content)