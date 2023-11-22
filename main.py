from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insults.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# set up insult class
class Insult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    # add more fields here as needed, such as timestamps, user IDs, etc.

    def __repr__(self):
        return '<Insult %r>' % self.content

# initalise db

with app.app_context():
    db.create_all()



@app.route('/add-insult', methods=['POST'])
def add_insult():
    content = request.form['content']
    new_insult = Insult(content=content)
    db.session.add(new_insult)
    db.session.commit()
    return "Insult added!"
