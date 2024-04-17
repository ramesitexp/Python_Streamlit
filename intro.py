#import the necessary modules
import streamlit as st
import pandas as pd

#Adding titles
st.title("Hello, welcome to the Python")

#header
st.header("This is a header")

#adding sub headers
st.subheader("This is sub header")

Data= {
    "Company": ["google","Apple","Ineuron"],
    "price": ["100","200","300"],
    "Language": ["Python","java","C++"]
}

st.write(Data)

st.write(pd.DataFrame(Data))

## markdown 

st.markdown("""This is a markdown file
# h1 tag 
## h2 tag
### h3 tag """) 