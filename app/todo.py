from todo_manager import TodoManager
import os
import sys
import datetime


def clear_screen():
    """
    Clears the cli screen
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("--------------------------------------------------------------------------------------------")


def format_todo_date(original_date: str) -> str:
    """
    Takes an expected string of
    2024-05-11 03:42:02
    and turns it into
    May 11, 2024
    :param original_date: The original date string that's in the db
    """
    original_date_datetime = datetime.datetime.strptime(
        original_date, "%Y-%m-%d %H:%M:%S"
    )
    formatted_date = original_date_datetime.strftime("%B %d, %Y")
    formatted_date = formatted_date.replace(" 0", " ")
    return formatted_date 


def prompt_user() -> str:
    """
    The text that prompts the user
    """
    print("What would you like to do? Enter a, b, c, or d\n")
    print("a) Create new todo.\n")
    print("b) Update existing todo.\n")
    print("c) Delete a todo.\n")
    print("d) Exit\n")
    return input("")


def prompt_actions(option: str) -> str:
    """
    Prompts the user on 1 of 4 options. a, b, c, or d
    :param option: The option the user selects
    """
    todo = TodoManager()
    # If user wants to create a new todo item 
    if option.lower() == "a":
        clear_screen()
        title = input("What is the name/title of your todo item?\n")
        description = input(
            "What is the description of your todo item? Press enter if you don't want a description\n"
        )
        if description:
            todo.create_todo(title, description)
        else:
            todo.create_todo(title)

        todos = todo.read_todos()
        todo.close_db()
        latest_todo = todos[-1]
        clear_screen()
        print(f"Created todo item number {latest_todo[0]}...\n")
    # If user wants to update a todo item 
    elif option.lower() == "b":
        clear_screen()
        todo_id = input("What is the ID of the todo item?\n")
        try:
            todos = todo.read_a_todo(todo_id)
            title = input(f"What is the name/title of your todo item? Original was '{todos[0][1]}'\n")
            description = input(
                f"What is the description of your todo item? Original was '{todos[0][2]}' Press enter if you don't want a description\n"
            )
            if description:
                todo.update_todo(todo_id, title, description)
                clear_screen()
            else:
                todo.update_todo(todo_id, title)
                clear_screen()
        except:
            clear_screen()
            print(f"Sorry, there seems to be no todo item with id of {todo_id}...\n")
        
        todo.close_db()
    # If user wants to delete a todo item 
    elif option.lower() == "c":
        clear_screen()
        todo_id = input("What is the ID of the todo item that you want to delete? Or type 'all' to delete all todo items\n")
        try:
            if todo_id == "all":
                todo.read_todos()
                confirmation_decision = input("Are you sure you want to delete all todo items? Type 'y' to confirm or 'n' to deny\n")
            else:
                todos = todo.read_a_todo(todo_id)
                print(f"\nID: {todos[0][0]}\n{todos[0][1]}\nDescription: {todos[0][2]}\nDate Created: {format_todo_date(todos[0][3])}\n\n")
                confirmation_decision = input("Are you sure you want to delete the above todo item? Type 'y' to confirm or 'n' to deny\n")
            
            if confirmation_decision == "y" and todo_id == "all":
                todo.delete_todo(todo_id)
                clear_screen()
            else:
                todo.delete_todo(todo_id)
                clear_screen()
        except:
            clear_screen()
            print(f"Sorry, there seems to be no todo item with id of {todo_id}...\n")
        
        todo.close_db()
    # If user wants to exit cli program 
    elif option.lower() == "d":
        clear_screen()
        print("See you later!")
        sys.exit(0)
    # If user enters some wild stuff 
    else:
        clear_screen()
        print(f"I'm sorry, I don't know the '{option}' command\n\n")


def list_todos() -> str:
    """
    Formats the todo items into a nice view in the cli
    """
    todo = TodoManager()
    todos = todo.read_todos()
    clear_screen()
    if len(todos) > 0:
        intro = "Your Todo Items\n\n"
        todos_formatted_string = ""
        for todo in todos:
            todos_formatted_string = (
                todos_formatted_string
                + f"ID: {todo[0]}\n{todo[1]}\nDescription: {todo[2]}\nDate Created: {format_todo_date(todo[3])}\n\n"
            )

        return intro + todos_formatted_string
    else:
        return "\nYou currently have no todo items...\nChange that with option 'a' below!\n"

if __name__ == '__main__':
    running = True
    while running:
        print(list_todos())
        user_prompt = prompt_user()
        prompt_actions(user_prompt)
