from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))


    #Create new author
    new_author = Author.create(author_name) 
    print(f"New Author created with ID: {new_author.id}")

    #Verify the author is added to the database
    retrieved_author = Author.get_by_id(new_author.id) 
    if retrieved_author: 
        print(f"Retrieved Author: {retrieved_author.name}") 
    else: 
        print("Author retrieval failed")

    #Attempt to change the name(should print an error message)
    new_author.name = "Jane Doe"

    #Delete the author
    Author.delete(new_author.id) 
    print(f"Author with ID {new_author.id} deleted")

    #Verify the author is deleted
    retrieved_author = Author.get_by_id(new_author.id) 
    if retrieved_author: 
        print(f"Failed to delete author: {retrieved_author}") 
    else: 
        print("Author deletion verified, not found")

    #Create new magazine
    new_magazine = Magazine(0, magazine_name, magazine_category)

    print(f"New Magazine created with ID: {new_magazine.id}")

    # Retrieve the magazine by ID
    retrieved_magazine = Magazine.get_by_id(new_magazine.id)
    if retrieved_magazine:
        print(f"Magazine_retrieved: {retrieved_magazine}")
    else:
        print("Failed to retrieve the magazine")

    # Update the magazine"s name
    new_magazine.name = "Tech Tomorrow" 
    print(f"Magazine updated: {new_magazine}")

    # Delete the magazine
    Magazine.delete(new_magazine.id) 
    print(f"Magazine with ID {new_magazine.id} deleted")

    #Verify the deletion
    retrieved_magazine = Magazine.get_by_id(new_magazine.id) 
    if retrieved_magazine: 
        print(f"Failed to delete magazine: {retrieved_magazine}") 
    else: 
        print("Magazine deletion verified")

    # Create new article
    new_article = Article(0, article_title, article_content, new_author.id, new_magazine.id) 
    print(f"New Article created with ID: {new_article.id}, Title: {new_article.title}")

    # Verify the article is added to the database
    retrieved_article = Article.get_by_id(new_article.id) 
    if retrieved_article: 
        print(f"Retrieved Article: {retrieved_article.title}") 
        print(f"Article Author: {retrieved_article.author.name}") 
        print(f"Article Magazine: {retrieved_article.magazine.name}") 
    else: 
        print("Article retrieval failed")

    # Test Author methods
    author_articles = new_author.articles() 
    print(f"Articles by {new_author.name}: {[article.title for article in author_articles]}")

    author_magazines = new_author.magazines() 
    print(f"Magazines associated with {new_author.name}: {[magazine.name for magazine in author_magazines]}")

    # Test Magazine methods
    magazine_articles = new_magazine.articles() 
    print(f"Articles in {new_magazine.name}: {[article.title for article in magazine_articles]}")

    magazine_contributors = new_magazine.contributors() 
    print(f"Contributors to {new_magazine.name}: {[author.name for author in magazine_contributors]}")

    # Attempt to change the title(should print error message)
    new_article.title = "AI in 2025"

    #Delete the article
    Article.delete(new_article.id) 
    print(f"Article with ID {new_article.id} deleted")

    # Verify the article is deleted
    retrieved_article = Article.get_by_id(new_article.id) 
    if retrieved_article: 
        print(f"Failed to delete article: {retrieved_article}") 
    else: 
        print("Article deletion verified, not found")



if __name__ == "__main__":
    main()
