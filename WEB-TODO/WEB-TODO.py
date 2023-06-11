import streamlit as st
import web_functions

todos = web_functions.get_todos()


def add_todo():
    """
    Callback function for adding a new TODO.

    Reads the value from the 'new_todo' text_input, appends it to the 'todos' list,
    and clears the input field for the next entry.
    """
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local.title())
    web_functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('My TODO App')

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        """
        If the checkbox for a TODO is selected, remove the corresponding item from the 'todos' list,
        update the persistent storage with the modified 'todos' list,
        remove the state associated with the TODO from the session state,
        and trigger a rerun of the Streamlit app to reflect the changes.
        """
        todos.pop(i)
        web_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new TODO',
              on_change=add_todo, key='new_todo')
