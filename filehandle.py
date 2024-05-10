# import numpy as np
# import streamlit as st
# import pandas as pd

# st.write('''
# # Simple Machine Learning Web Application

# Need to upload a file of 500-900 MB size  
# to see if the streamlit can handle the file

# ''')


# try:
#     file = st.file_uploader("Upload the file")
# except: 
#     if file != None:
#         st.video(file)
#     else:
#         print("Please upload the file") 


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.write('''
# Simple Machine Learning Web Application

Need to upload a file of 500-900 MB size  
to see if the streamlit can handle the file
''')

try:
    file = st.file_uploader("Upload the file")
    if file is not None:
        st.video(file)
    else:
        st.write("Please upload the file")
except Exception as e:
    st.error(f"An error occurred: {e}")

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)