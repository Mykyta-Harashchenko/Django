Quotes Manager Django Project
Quotes Manager is a Django-based web application that allows users to manage and interact with quotes, authors, and tags. The app supports features like selecting a quote of the day, retrieving a random quote, and categorizing quotes with tags. This project provides both a web interface and API endpoints for managing quotes and authors.

This project allows users to:
Add, edit, and delete quotes.
Assign quotes to authors.
Tag quotes for easier categorization.
Set a "Quote of the Day" (automatically displayed each day).
Retrieve a random quote at any time.
Filter quotes by tags or authors.

The project leverages Django for backend logic, with Django REST Framework for API support and JWT tokens for authentication.

Features

Quote Management:
Add, edit, and delete quotes with associated authors and tags. Each quote can have multiple tags for better categorization.

Quote of the Day:
Select a specific quote as the "quote of the day" and retrieve it dynamically.

Random Quote:
Retrieve a random quote at any time, providing inspiration or motivation.

Tagging System:
Tags help categorize quotes. Users can filter quotes by one or more tags.

Author Management:
Manage authors who contribute quotes. Each author can have multiple quotes.

User Authentication:
Users can log in, register, and authenticate using JWT tokens for secure sessions.

Admin Interface:
The Django admin interface allows easy management of authors, quotes, and tags.

Tech Stack

Backend:
Django (Web framework)
Django REST Framework (For building APIs)
JWT (Authentication using JSON Web Tokens)
PostgreSQL (Database for storing quotes, authors, and tags)

Frontend (If applicable):
Javascript
HTML
CSS

Getting Started

Prerequisites
Ensure you have the following installed on your machine:
Python 3.8+: Download here
PostgreSQL (or any other relational database, but PostgreSQL is recommended)
Docker (for containerization, optional)

Installation
Clone the repository:
git clone https://github.com/Mykyta-Harashchenko/Django.git
Navigate to the project directory:
cd Django

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Set up the database:
Configure your PostgreSQL database (or another database) and update DATABASES in settings.py.
Run the migrations to set up your database schema:
python manage.py migrate

Run the development server:
python manage.py runserver

The app should now be running at http://localhost:8000.

API Endpoints
This project exposes several API endpoints to interact with quotes, authors, and tags.

Authentication
POST /api/auth/signup
Register a new user.

POST /api/auth/login
Log in and receive a JWT token.

Quotes
GET /api/quotes
Retrieve all quotes (supports pagination).

POST /api/quotes
Add a new quote (requires authentication).

GET /api/quotes/{quote_id}
Retrieve a specific quote by its ID.

PUT /api/quotes/{quote_id}
Edit an existing quote.

DELETE /api/quotes/{quote_id}
Delete a quote.

GET /api/quote_of_the_day
Retrieve the current quote of the day.

GET /api/random_quote
Retrieve a random quote.

Authors
GET /api/authors
Retrieve all authors.

GET /api/authors/{author_id}
Retrieve all quotes by a specific author.

Tags
GET /api/tags
Retrieve all tags.

GET /api/tags/{tag_id}/quotes
Retrieve quotes associated with a specific tag.

Usage
Once your server is running, you can interact with the app through the web interface or API:

Sign Up: Register a new user account via the API or web interface.
Login: Log in using your credentials and obtain a JWT token.
Add Quotes: Add new quotes associated with authors and tags.
Tag Quotes: Organize quotes with tags for easy filtering.
Get Quote of the Day: View the current quote of the day.
Get Random Quote: Get a random quote at any time.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, feel free to contact us:
GitHub: https://github.com/Mykyta-Harashchenko
Thank you for exploring the Quotes Manager Django Project! We hope you enjoy using and contributing to the platform. Happy coding! 🚀
