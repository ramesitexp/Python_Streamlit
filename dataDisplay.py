#import the necessary modules
import streamlit as st
import pandas as pd
import numpy as np

#Dataframe 
df=pd.DataFrame(np.random.randn(50,20),
                columns=('col %d' %i for i in range(20)))

st.table(df)
# metrics 
st.metric(label="temperature",value="70 F",delta="1.2 F")

# st.metric looks especially nice in combination with st.columns:

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# The delta indicator color can also be inverted or turned off 
st.metric(label="Gas price", value=4, delta=-0.5,
     delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
     delta_color="off")

# st.json

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })