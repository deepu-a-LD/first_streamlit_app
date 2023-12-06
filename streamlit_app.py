import streamlit
streamlit.title('First demo with streamlit was successfull')
streamlit.header('Breakfast menu')
streamlit.text('Idly vada sambar')
streamlit.text('Dosa chatni')
streamlit.text('Puri curry')

streamlit.header('Build your own Fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
