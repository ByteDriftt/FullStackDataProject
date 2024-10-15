# FullStackDataProject

Full Stack Todo Application

Overview

This project is a full-stack web application for managing todo lists. It utilizes PostgreSQL for data storage, Flask for backend logic, and HTML templates with JavaScript for the frontend. The goal of the project was to learn and implement core web development concepts, including database interactions, API endpoints, and CRUD operations.

Technologies Used

PostgreSQL: Our database system, responsible for storing all persistent data.

Python & Flask: Python was used as the programming language, with Flask as the web framework to handle routing and server-side logic.

SQLAlchemy: An Object-Relational Mapper (ORM) used to interact with PostgreSQL using Python code rather than direct SQL queries.

Flask-Migrate: A tool to manage database schema changes through versioned migrations.

HTML, CSS, JavaScript: HTML templates were used for frontend layouts, with JavaScript for dynamic user interactions.

Key Features

Database Setup: PostgreSQL serves as the backend database. A schema file (schema.sql) defines the database structure, while a seed file (seed.sql) provides initial data.

Data Models: Defined data models using SQLAlchemy to represent the tables in the database.

CRUD Operations: Implemented functionality to create, read, update, and delete todos, allowing full interaction with the data.

Flask Routes: Created routes to manage incoming requests and serve different pages of the application.

Database Migrations: Used Flask-Migrate for managing changes to the database schema over time.

Front-End Interface: Built dynamic and user-friendly pages with HTML templates. Added JavaScript for seamless updates, such as deleting todos without refreshing the page.

Relationships: Established relationships between TodoList and Todo to ensure data is structured logically.

How It Works

The application starts a web server using Flask.

Routes define how requests are handled, whether they need to interact with the database or simply render a page.

SQLAlchemy translates Python code into SQL commands to communicate with PostgreSQL.

Flask-Migrate tracks changes to the database schema, similar to version control but for the database.

The HTML templates combined with Flask's rendering create the user interface, while JavaScript adds interactivity without needing a full page reload.

Summary

This project showcases my understanding of full-stack web development, including setting up a database, creating an API, developing a frontend, and handling interactions dynamically. It emphasizes separation of concerns, modularity, and the use of modern development tools and frameworks to build a functional, data-driven web application.