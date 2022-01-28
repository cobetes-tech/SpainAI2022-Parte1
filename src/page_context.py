import streamlit as st

def context():


    text =  """
            # Contexto
            Aquí escribimos el contexto, que es el fragmento de texto de la intranet sobre el cual queremos hacer preguntas.
            Como el modelo funciona en inglés, no queda otra que tirar de Google Translator o similar.
            """
    st.write(text)

    label = "Pega aquí el texto de la intranet"
    context_text = st.text_area(label, "")

    if context_text:
        text = "*¡Contexto listo!*"
        st.write(text)

    text = "---"
    st.write(text)

    text = """
           # Texto de ejemplo:

           In Brown Disp. Entertainment we pride ourselves on having a competitive remuneration model that meets the highest market standards. 
           That is why in addition to the salary of the payroll, we have a wide remuneration package with food aid such as restaurant tickets, reduced hours both in the summer months (July and August) and on Fridays. 
           We also have social benefits such as help with internet connection, discounts at the gym or optional medical insurance. 
           Likewise, in order to promote training and constant learning, all employees have a budget of € 1,200 per year to dedicate to courses and conferences.
           """
    st.write(text)

    st.session_state['context_text'] = context_text