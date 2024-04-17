
import streamlit as st
import pandas as pd
import numpy as np

# button 
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

# checkbox 

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')

# radio button 

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

# selectbox

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# multiselect 

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# slider 

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# An Example of a range slider 
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#  Range Slider 
from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Datetime Slider 

from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
