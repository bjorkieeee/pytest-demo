import sqlite3


class TodoManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("app/todos.db")
        self.cursor = self.conn.cursor()

    def check_db_connection(self) -> bool:
        """
        If the db is connected, then we return True. If not we return False
        :return: True or False
        """
        if self.conn:
            return True
        return False
    
    def create_todo_table(self):
        """
        Function to create the TODO table with all the proper keys
        Only needs to be ran once
        """
        self.cursor.execute(
            "CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT, description TEXT, date DATETIME);"
        )

    def create_todo(self, title: str, description=None):
        """
        Function to crate a TODO item
        :param title: Title/name of the todo item as a string
        :param description: Description as a string or None
        """
        self.cursor.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)", (title, description)
        )
        self.conn.commit()

    def read_todos(self):
        """
        Function to read all TODO items
        """
        self.cursor.execute("SELECT * FROM todos")
        todos = self.cursor.fetchall()
        return todos
    
    def read_a_todo(self, todo_id):
        """
        Function to read a specific TODO item
        :param todo_id: ID of a specific todo item
        """
        self.cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id))
        todo = self.cursor.fetchall()
        return todo 

    def update_todo(self, todo_id, title, description=None):
        """
        Function to update a TODO item
        :param todo_id: ID of a specific todo item
        :param title: New title of the todo item as a string
        :param description: New description of the todo item as a string
        """
        self.cursor.execute(
            "UPDATE todos SET title = ?, description = ? WHERE id = ?",
            (title, description, todo_id),
        )
        self.conn.commit()

    def delete_todo(self, todo_id):
        """
        Function to delete a TODO item. You can put in "all" as the todo_id to delete all rows
        :param todo_id: ID of a specific todo item
        """
        if todo_id == "all":
            self.cursor.execute("DELETE FROM todos")
        else:
            self.cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
            self.conn.commit()

    def close_db(self):
        """
        Closes the connection to the db
        """
        self.conn = self.conn.close()

