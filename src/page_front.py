import streamlit as st


def front():

    text = """
            # ¡Oh, un modelo de ML, vamos a desplegarlo! - Machine learning para adultos 
            
            ¡Enhorabuena por llegar a uno de los talleres más molones de Spain AI 2022!
            
            Hoy vas a trastear con:

            1. **NLP**, que son las siglas de Natural Language Processing. No tiene nada que ver con Neuro-Linguistic Programming.
            2. Arquitecturas de redes neuronales basadas en **Transformers** (usando la famosa librería **HuggingFace**).
            3. Resolviendo la tarea conocida como "**Extractive Question Answering**".
            4. Y poniendo en producción un modelo de Machine Learning usando **Streamlit** y **Heroku**.

            ---

            Si tienes cualquier duda, aquí tienes los nombres e emails de los ponentes, pregunta sin miedo :) 
            * Ricardo Guerrero: [ricgu8086@gmail.com](mailto:ricgu8086@gmail.com)
            * Enrique Josue Álvarez: [ejarkm@gmail.com](mailto:ejarkm@gmail.com)
            * Lino Figueroa: [impalah@gmail.com](mailto:impalah@gmail.com)
            """
    st.write(text)

    image_huggingface_url = "https://avatars.githubusercontent.com/u/25720743?s=200"
    st.image(image_huggingface_url)

    text = "HuggingFace"
    url = "https://huggingface.co/"
    link = "[%s](%s)" % (text, url)
    st.write(link)
