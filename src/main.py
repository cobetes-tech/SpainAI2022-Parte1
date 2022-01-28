import streamlit as st

from page_sidebar import sidebar
from page_front import front
from page_task import task
from page_download_model import download_model
from page_context import context
from page_questions import questions
from page_results import results
from page_cheatsheet import cheatsheet
from page_your_turn import your_turn


def main():

    pages_mapper = {
                        '1. Portada': front,
                        '2. ¿Qué vamos a hacer?': task,
                        '3. Descargar un modelo': download_model,
                        '4. Contexto': context,
                        '5. Preguntas': questions,
                        '6. Resultados': results,
                        '7. Chuleta': cheatsheet,
                        '8. Os toca': your_turn
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()