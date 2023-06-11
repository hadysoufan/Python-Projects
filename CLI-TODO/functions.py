def get_todos(filepath='todos.txt'):
    """
    Retrieves a list of todos from a file.

    Args:
        filepath (str): Path to the file containing todos. Default is 'todos.txt'.

    Returns:
        list: List of todos read from the file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_args, filepath='todos.txt'):
    """
    Writes a list of todos to a file.

    Args:
        todos_args (list): List of todos to be written.
        filepath (str): Path to the file to write todos. Default is 'todos.txt'.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


if __name__ == '__main__':
    print('Hello from function')
    print(get_todos())
