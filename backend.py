import sqlite3


class Databse:

    # Creating and connecting to the database
    def __init__(self):
        self.connection = sqlite3.connect('books.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connection.commit()

    # Insert function
    def insert(self,title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.connection.commit()

    # View function
    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows

    # Search function
    def search(self,title='', author='', year='', isbn=''):
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    # Delete function
    def delete(self,id):
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.connection.commit()

    # Update function
    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.connection.commit()

    # Closing the connection to the db by destroying the object
    def __del__(self):
        self.connection.close()

