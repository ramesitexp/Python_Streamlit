#import the necessary modules 
import streamlit as st
import pandas as pd

#Adding titles
st.write("Hello **world**!")

#magic command 
"Hello **world**!"

#st.caption
st.caption("This is s string")

# st.code 
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

#st.text 
st.text("This is python text")

# st.latex 

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
