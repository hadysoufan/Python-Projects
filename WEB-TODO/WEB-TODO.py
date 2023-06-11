import streamlit as st
import web_functions

todos = web_functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local.title())
    web_functions.write_todos(todos)


st.title('My TODO App')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new TODO',
              on_change=add_todo, key='new_todo')
