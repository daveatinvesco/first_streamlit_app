import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🫐 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('Avocado 🥑 toast')

streamlit.header('Build your own fruit Smoothie 🍓🍇🍑')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list..set_index('Fruit')

streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
