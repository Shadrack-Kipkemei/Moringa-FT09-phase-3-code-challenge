import sqlite3
from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self.name = name
        self.category = category
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
        if isinstance(value, int):
            self._id = value
        else:
            print("ID must be an integer.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print("Name must be a string between 2 and 16 characters inclusive.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print("Category must be a non-empty string.")

    def __repr__(self):
        return f'<Magazine {self.name} ({self.category})>'

    @classmethod
    def get_by_id(cls, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['name'], row['category'])

    @classmethod
    def delete(cls, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM magazines WHERE id = ?', (magazine_id,))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            print(f"No magazine found with ID {magazine_id}")

    def articles(self):
        from models.article import Article  # Local import to avoid circular dependency
        # Fetch all articles associated with the magazine using SQL JOIN
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT articles.id, articles.title, articles.content, articles.author_id, articles.magazine_id
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        ''', (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) for row in rows]

    def contributors(self):
        from models.author import Author  # Local import to avoid circular dependency
        # Fetch all authors associated with the magazine using SQL JOIN
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        ''', (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row['id'], row['name']) for row in rows]
