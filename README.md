## Article Management System


This is an Article Management System that allows users to manage authors, magazines, and articles in a relational database. It uses SQLite as the database and provides an easy-to-use interface for creating and managing authors, magazines, and articles.

## Features

* Create and manage authors and magazines.
* Add articles with titles, content, and associated authors and magazines.
* Query articles, authors, and magazines with relationships between them.
* Manage relationships between articles and their respective authors and magazines.


## Technologies Used

* Python: The main programming language.
* SQLite3: The relational database used to store authors, magazines, and articles.
* SQLAlchemy (optional): If you wish to use it for ORM-based operations, the project can be extended for that purpose.


## Installation

# Prerequisites
* Python 3.x (Ensure that Python is installed on your machine)

# Steps to Install:
1. Clone the repository:

git clone https://github.com/Shadrack-Kipkemei/Moringa-FT09-phase-3-code-challenge
cd Moringa-FT09-phase-3-code-challenge

2. Install required packages: You can use pip to install dependencies. It is recommended to use a virtual environment for better isolation:


## Usage

1. Run the Application: You can run the application using the following command:

python3 app.py

2. Interact with the system:
* The application will prompt you to enter details for authors, magazines, and articles.
* You will be asked to input:
  * Author’s name
  * Magazine’s name and category
  * Article title and content

3. View Results: After entering the information, the application will display the inserted records for authors, magazines, and articles. It will also demonstrate the relationships between articles, authors, and magazines.


## Database Schema

The database schema consists of three main tables:
* authors: Stores author details.
* magazines: Stores magazine details.
* articles: Stores articles, linked to authors and magazines via foreign keys.


## Code Structure
* app.py: The main script that runs the application and prompts the user for input.
* database/connection.py: Manages database connections.
* database/setup.py: Contains the logic to create the necessary tables in the database.
* models/: Contains the classes (Article, Author, and Magazine) that represent entities in the database and their relationships.

## Contributing

Feel free to fork the repository, submit issues, or create pull requests. If you have suggestions or improvements, don't hesitate to contribute!

## License

The content of this project is licensed under the MIT license Copyright (c) 2024.
