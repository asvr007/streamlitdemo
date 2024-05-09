import streamlit as st

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
