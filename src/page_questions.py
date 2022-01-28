import streamlit as st

def questions():

    text =  """
            # ¿Qué queremos preguntar?
            """

    st.write(text)


    question1_text = "Pregunta 1: "
    question2_text = "Pregunta 2: "
    question3_text = "Pregunta 3: "
    default_text = ""

    question1 = st.text_input(question1_text, default_text)
    question2 = st.text_input(question2_text, default_text)
    question3 = st.text_input(question3_text, default_text)
    questions_text = [question1, question2, question3]

    if all(questions_text):
        text = "*¡Preguntas listas!*"
        st.write(text)

    text = "---"
    st.write(text)

    text = """
           # Preguntas de ejemplo:

           * When is the reduced day?
           * What is the training budget?
           * What are the social benefits?
           """

    st.write(text)

    # Save state
    st.session_state['questions_text'] = questions_text