import sqlite3
from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self.title = title  # Use the setter to validate and set the title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        if self._id == 0:
            self.save()

    def save(self):
        # Save the article to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self._title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        self._id = cursor.lastrowid  # Set the id after inserting the article
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Ensure title is a string between 5 and 50 characters inclusive
        if hasattr(self, '_title'):
            print("Title cannot be changed once set.")
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            print("Title must be a string between 5 and 50 characters inclusive.")

    def __repr__(self):
        return f'<Article {self.title}>'

    @classmethod
    def get_by_id(cls, article_id):
        # Retrieve an article by ID from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id'])

    @classmethod
    def delete(cls, article_id):
        # Delete an article by ID from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            print(f"No article found with ID {article_id}")
