"""
Starting Point for the Flask App

This file sets up our Flask app. Think of it like the heart of our application.
It's where we make our Flask app ready to run and tell it about other parts 
like the database and web page routes.

What Happens Here:
- We make a new Flask app.
- We tell the app about our settings (like where the database is).
- We get the app ready to work with the database using SQLAlchemy. This means 
  our app can save and load data from the database.
- If we have blueprints (groups of routes), we add them here.

How it Connects to Other Files:
- models.py: This file uses models.py to understand our database structure.
- routes.py: It adds the routes from routes.py, so our app knows what to do when 
  people visit different pages.
- Any other setups like error pages or extra tools (extensions) are also added here.

When to Use This File:
- Import this file in other parts of our project when we need to use the app itself 
  or anything we set up here (like the database).

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insults.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set a secret key for session management - make this an env variable for prod
app.config['SECRET_KEY'] = 'your_very_secret_key_here'

db = SQLAlchemy(app)

from app import routes  # Import routes after creating the app

with app.app_context():
    db.create_all()  # Initialize the database
