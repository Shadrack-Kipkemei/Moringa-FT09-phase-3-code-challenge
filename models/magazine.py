import sqlite3
from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        # Initialize the magazine with an id, name, and category
        self._id = id
        self.name = name  # Using the setter to validate and set the name
        self.category = category  # Using the setter to validate and set the category
        self.save()

    def save(self):
        # Save the magazine to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        # Ensure id is of type int
        if isinstance(value, int):
            self._id = value
        else:
            print("ID must be an integer.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Ensure name is a string between 2 and 16 characters inclusive
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print("Name must be a string between 2 and 16 characters inclusive.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Ensure category is a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print("Category must be a non-empty string.")

    def __repr__(self):
        return f'<Magazine {self.name} ({self.category})>'

    @classmethod
    def get_by_id(cls, magazine_id):
        # Retrieve a magazine by ID from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['name'], row['category'])

    @classmethod
    def delete(cls, magazine_id):
        # Delete a magazine by ID from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM magazines WHERE id = ?', (magazine_id,))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            print(f"No magazine found with ID {magazine_id}")
