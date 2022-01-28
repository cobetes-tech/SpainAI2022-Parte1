import streamlit as st

def cheatsheet():

    text = "# Comandos que nos pueden ser de ayuda:"
    st.write(text)


    title = "1. Write"
    expander = st.expander(title)
    text = "*st.write* Te sirve para escribir cualquier cosa: texto, variables, resultados de operaciones, dataframes \
             (aunque hay una mejor alternativa para los dataframes), ... Lo mejor de todo es que también acepta \
            sintáxis Markdown. Aquí tenéis una [chuleta](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), \
            por si quieres probar."
    expander.write(text)

    title = "2. Image"
    expander = st.expander(title)
    text = "*st.image* Te sirve para mostrar imágenes de internet. Solo tienes que pasarle la dirección URL."
    expander.write(text)

    title = "3. Button"
    expander = st.expander(title)
    text = """
            *st.button* Te sirve para activar acciones. Con ello puedes ejecutar funciones de código, mostrar contenido nuevo, etc.

            ```python
            pressed = st.button("Saludar")

            if pressed == True:
                st.write("Hola mundo)
            ```
            """
    expander.write(text)

    title = "4. Expand"
    expander = st.expander(title)
    text = "*st.expander* Te sirve para generar estas cajitas desplegables tan chulas que estás usando ahora. Perfecto para no hacer spoilers"
    expander.write(text)

    title = "5. Sidebar"
    expander = st.expander(title)
    text = "*st.sidebar* Te permite crear una barra lateral en la que puedes usar todos los comandos que quieras: botones, imágenes, \
        desplegables... Es perfecto para hacer un menú de navegación."
    expander.write(text)

    title = "6. Selectbox"
    expander = st.expander(title)
    text = """
            *st.selectbox* Te sirve para pedirle al usuario que escoja entre varias opciones. Se abre un desplegable con una lista predefinida
            Ejemplo:

            ```python
            option = st.sidebar.selectbox("Escoge", [1, 2, 3, 4])

            if option == 1:
                expander = st.expander("Saber más"):
                expander.write("Habia una vez un circo")
            else:
                st.write("Te recomiendo escoger la opción 1")
            ```
            """
    expander.write(text)

    title = "7. Dataframe / table"
    expander = st.expander(title)
    text = "*st.dataframe* / *st.table* Aunque puedes usar *st.write*, para este caso concreto te recomiendo mucho más usar *st.dataframe* o *st.table*, \
            a nivel visual queda mucho más molón."
    expander.write(text)


    text =  """
            ## Y si necesitas algo más:

            1. Puedes mirar el código de esta aplicación, que tiene muchos componentes de ejemplo.
            2. O puedes preguntarnos.
            3. O puedes consultar la documentación de Streamlit [aquí](https://docs.streamlit.io/en/stable/api.html).

            Lo que tú prefieras :-)
            """
    st.write(text)
