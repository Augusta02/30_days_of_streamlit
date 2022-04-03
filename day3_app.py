# first import streamlit
import streamlit as st

# create web app header
st.header('Creating Streamlit button')


if st.button('Say hello'):
    # button displays input Say hello
    # st.write function is used to print messages
    st.write('Why hello there')


else:
    st.write('Goodbye')
