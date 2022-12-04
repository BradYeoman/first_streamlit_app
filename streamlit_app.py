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
my_fruit_list = my_fruit_list.set_index('Fruit')

# add a pick list here so users can pick the fruit
# they want to include in their smoothie
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
st.dataframe(fruits_to_show)
