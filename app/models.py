"""
models.py: Where We Define Our Database Tables

Think of this file as the blueprint for our database. Here, we describe what data we 
want to store and how it should be organized. We use SQLAlchemy, which is a tool that 
helps our app talk to the database in an easy way.

What's Inside:
- We define 'classes' here. Each class is like a blueprint for a table in the database.
- For example, if we have an 'Insult' class, it means we'll have an 'insults' table 
  in the database.
- Each class has 'fields' (like columns in a table). For an insult, this might be 
  'content' of the insult and an 'id' as a unique identifier.

How it Connects to Other Files:
- __init__.py: The app made in __init__.py uses these definitions to create real 
  tables in our database.
- routes.py: When we add, remove, or change data in our routes, we're using these 
  classes to tell the database what to do.

When to Use This File:
- Use this file when you need to define a new type of data to store or when you 
  need to understand what data we are storing and how.

"""

from datetime import datetime
from app import db

class Insult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    added_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    approved_status = db.Column(db.String(50), default='Queued')

    def __repr__(self):
        return f'<Insult {self.content}>'



