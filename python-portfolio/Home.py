import streamlit as st
import pandas

st.set_page_config(layout="wide")



st.image('images/photo.png')
st.title('Taiwo Akinnusoye')
content = """Hi, I'm Taiwo. I am a full stack software engineer. 
    You'll find stuff I have worked on or working on in Python here."""
st.info(content)



col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

csv_dataframe = pandas.read_csv('data.csv', sep=";")

with col3:
    for index, row in csv_dataframe[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://github.com/taiwo-eng/Python36Zero)")

with col4:
    for index, row in csv_dataframe[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://github.com/taiwo-eng/Python36Zero)")