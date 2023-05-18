def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        local_todos = file_local.readlines()
    return local_todos


''' This function get the filepath as todos.tx and opens it with read permissions'''


def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


'''This function gets the filepath and opens it with write permissions'''
