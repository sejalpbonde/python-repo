while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a Todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")

        case 'edit':
            number = int(input("Enter the number of TODO you want to edit: "))
            number = number - 1
            new_todo = input("Enter new TODO: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the TODO to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break

        case _:
            print("Hey, you have entered an unknown command")
print("Bye!")
