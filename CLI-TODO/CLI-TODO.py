from functions import get_todos, write_todos
import time

time_now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'Time now: {time_now}')

while True:
    """
    A simple TODO list application.
    Allows the user to view, add, edit, and remove TODO items.

    Commands:
    - show: Display all TODO items.
    - add: Add a new TODO item.
    - edit: Edit an existing TODO item.
    - remove: Remove a TODO item.
    - exit: Exit the application.
    """

    user_action = input('Enter show, add, edit, remove, or exit TODOS: ')
    user_action = user_action.strip()

    if user_action.startswith('show'):
        todos = get_todos()

        for i, todo in enumerate(todos):
            print(f'TODO {i + 1}: {todo.strip()}')

        print(f'Count of TODOS = {len(todos)}')

    elif user_action.startswith('add'):
        try:
            todos = get_todos()

            todo = user_action[4:] + '\n'

            todos.append(todo.capitalize())

            write_todos(todos)

        except ValueError:
            print(f'Command is unavailable')

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()

            todo_number = int(user_action[5:])

            try:
                if todo_number > len(todos) or todo_number <= 0:
                    raise IndexError

                new_todo = input('Enter new TODO: ') + '\n'
                todos[todo_number - 1] = new_todo.capitalize()

                write_todos(todos)

                print(f'TODO "{new_todo.capitalize().strip()}" was edited successfully')

            except IndexError:
                print(f'TODO number "{todo_number}" is Invalid')

        except ValueError:
            print('Command is unavailable')

    elif user_action.startswith('remove'):
        try:
            todos = get_todos()

            todo_number = int(user_action[7:])

            try:
                if todo_number > len(todos) or todo_number <= 0:
                    raise IndexError

                removed_todo = todos.pop(todo_number - 1).strip()

                write_todos(todos)

                print(f'TODO "{removed_todo.capitalize()}" was removed successfully')

            except IndexError:
                print(f'TODO number "{todo_number}" is unavailable')

        except ValueError:
            print('Command is unavailable')

    elif user_action.startswith('exit'):
        break

    else:
        print(f'Command "{user_action}" is Invalid command')

print('GOOD BYE')
