import streamlit
streamlit.title('First demo with streamlit was successfull')
streamlit.header('Breakfast menu')
streamlit.text('Idly vada sambar')
streamlit.text('Dosa chatni')
streamlit.text('Puri curry')

streamlit.header('Build your own Fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
