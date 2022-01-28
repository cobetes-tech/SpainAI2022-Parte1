import streamlit as st
import pandas as pd
import pylab as plt
import seaborn as sns


def user_interface():

    text =  """
            # Y estas son las respuestas
            ¿Habrá funcionado?
            """
    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed


def logic():

    try:
        nlp = st.session_state['nlp_model']
        context = st.session_state['context_text']
        questions = st.session_state['questions_text']

    except KeyError:

        st.write(st.session_state)

        text =  """
                Completa los pasos en orden, porfi.

                Necesitamos configurar un modelo, unas preguntas y un contexto antes de seguir.
                """
        st.write(text)
        return

    results = []

    for question in questions:

        inp = {
                  "question": question,
                  "context": context
              }

        res = nlp(inp)

        results.append(res)

    # Formatting tabular results
    results_df = pd.DataFrame(results)
    results_df['question'] = questions
    results_df['score'] = 100*results_df['score']
    selected_cols = ['question', 'answer']
    results_df2 = results_df[selected_cols]

    st.table(results_df2)

    # Plotting score
    title = "¿Cuanto nos fiamos de las respuestas?"
    expander = st.expander(title)
    
    fig = plt.figure(1)
    _ = plt.title("¿Cuanto nos fiamos de la respuesta?")
    _ = sns.barplot(x='score', y='question', data=results_df, orient='h')
    _ = plt.grid(True)
    _ = plt.xlim(0, 100)

    expander.pyplot(fig)

    # Intranet text for user manual inspection
    text = "Texto de la intranet"
    expander = st.expander(text)
    expander.write(context)


def results():

    pressed = user_interface()

    if pressed:
        logic()