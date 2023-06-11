import streamlit as st
import web_functions

todos = web_functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local.title())
    web_functions.write_todos(todos)


st.title('My TODO App')

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(i)
        web_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new TODO',
              on_change=add_todo, key='new_todo')
