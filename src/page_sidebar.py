import streamlit as st

def sidebar(ls_page_name):

    # Resources
    image_pyconlogo_url = "https://pbs.twimg.com/profile_images/1379380435969527810/5RNBIJY9.jpg"
    edition = "PyConEs 2021"
    title = "# Vamos a explorar"

    st.sidebar.image(image_pyconlogo_url)
    st.sidebar.write(edition)
    st.sidebar.write(title)
    page_name = st.sidebar.selectbox("", ls_page_name)

    return page_name
