import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🫐 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('Avocado 🥑 toast')
streamlit.header('Build your own fruit Smoothie 🍓🍇🍑')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# pick list
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display
streamlit.dataframe(fruits_to_show)

# create a repeatable code block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# new section  
streamlit.header('Fruityvice fruit advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
#streamlit.write('The user entered', fruit_choice)
except URLError as e: 
  streamlit.error()

streamlit.header("View our fruit list - Add your favorites!")
# snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from FRUIT_LOAD_LIST")
         return my_cur.fetchall()
# add a button to load
#if streamlit.button('Get Fruit Load List'):
    
#    my_data_rows = get_fruit_load_list()
#    streamlit.dataframe(my_data_rows)
# streamlit.dataframe(my_data_rows)


# allow user to add fruit to the list 
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
        return "Thanks for adding " + new_fruit
        
add_my_fruit=streamlit.text_input('Get Fruit List')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    my_cnx.close()
    
#streamlit.text(fruityvice_response.json())
#take the json version 

#output 
# do not add anything past here
streamlit.stop()


my_cur = my_cnx.cursor()





# next 


