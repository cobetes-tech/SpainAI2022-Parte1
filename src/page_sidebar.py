import streamlit as st


def sidebar(ls_page_name):

    # Resources
    image_spainai_url = "https://www.spain-ai.com/wp-content/uploads/2021/04/cropped-spain_ai-150x150.png"
    edition = "Spain AI 2022"
    title = "# Vamos a explorar"

    st.sidebar.image(image_spainai_url)
    st.sidebar.write(edition)
    st.sidebar.write(title)
    page_name = st.sidebar.selectbox("", ls_page_name)

    return page_name
