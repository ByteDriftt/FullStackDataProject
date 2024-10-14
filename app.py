from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:eskisehir@localhost:5432/myproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user')
def add_user():
    new_username = f"new_user_{random.randint(1000, 9999)}"
    new_email = f"{new_username}@example.com"
    new_user = User(username=new_username, email=new_email)
    db.session.add(new_user)
    db.session.commit()
    return f"Added new user: {new_username}"

if __name__ == '__main__':
    app.run(debug=True)