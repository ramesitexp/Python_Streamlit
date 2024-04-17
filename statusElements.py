
import streamlit as st
import time
# example of a progress bar increasing over time:
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

# st.spinner

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

# st.ballons 
st.balloons()

# st.error

st.error('This is an error')

# st.warnings

st.warning('This is a warning')

# st.info 

st.info('This is a purely informational message')

# st.success 

st.success('This is a success message!')

# st.exception

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
