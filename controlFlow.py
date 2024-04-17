
import streamlit as st
import pandas as pd
import numpy as np

# st.stop 
# Streamlit will not run any statements after st.stop(). We recommend rendering a message to explain why the 
# script has stopped. When run outside of Streamlit, this will raise an Exception.

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

# st.form

# Inserting elements using "with" notation:

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Inserting elements out of order:

#form = st.form("my_form")
#form.slider("Inside the form")
#st.slider("Outside the form")

# Now add a submit button to the form:
#form.form_submit_button("Submit")
