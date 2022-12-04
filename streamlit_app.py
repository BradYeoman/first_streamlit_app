# import packages needed
import streamlit as st
import pandas as pd

# create main menu items
st.title('My Parent\'s New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🫐 🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥬 🥤 Kale, Spinach & Rockt Smoothie')
st.text('🐔 🥚 Hard-Boiled Free-Range Egg')
st.text('🥑 🍞 Avocado Toast')

st.header('🍌 🍓 Build Your Own Fruit Smoothie 🥝 🍇')

# load csv for fruits into pandas and display the dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
