todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a Todo: ")
            todos.append(todo)
        
        case 'show':
            for item in todos:
                print(item)
                
        case 'edit':
            number = int(input("Enter the number of TODO you want to edit: "))
            number = number - 1 
            new_todo = input("Enter new TODO: ")
            todos[number] = new_todo

        case 'exit':
            break

        case _:
            print("Hey, you have entered an unknown command")
print("Bye!")