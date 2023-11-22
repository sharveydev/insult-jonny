"""
routes.py: Defines What Happens on Each Page of Our App

In this file, we set up the 'routes'. These are like different pages or actions on our website. 
Each route is connected to a function that decides what happens when someone visits that page 
or performs that action.

What's Inside:
- We list different web addresses (like '/home' or '/add-insult') and what should 
  happen when someone goes to those addresses.
- Each function under a route is like an instruction manual for what the app should 
  show or do. For example, showing a list of insults, adding a new insult, etc.

How it Connects to Other Files:
- models.py: We use the structures from models.py to interact with the database. 
  Like getting data for insults or saving a new insult.
- __init__.py: This file uses routes.py to know all the pages and actions our app 
  handles.

When to Use This File:
- Update this file when you want to add a new page or a new action to your app.

"""
from flask import request, render_template, flash, url_for, redirect
from app import app, db
from app.models import Insult


@app.route('/insult')
def add_insult_form():
    return render_template('insult.html')

@app.route('/add-insult', methods=['POST'])
def add_insult():
    content = request.form['content'].strip()

    # Validate content length
    if not content or len(content) > 255:
        flash('Invalid insult length. Please keep it under 255 characters.')
        return redirect(url_for('add_insult_form'))

    try:
        new_insult = Insult(content=content)
        db.session.add(new_insult)
        db.session.commit()
        return render_template('insult_added_confirmation.html')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while adding the insult.')
        return redirect(url_for('add_insult_form'))

@app.route('/view-insults')
def view_insults():
    insults = Insult.query.all()  # Retrieve all insults from the database
    return render_template('view_insults.html', insults=insults)