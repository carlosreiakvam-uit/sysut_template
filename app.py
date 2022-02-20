from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from create_db import create_db
from db_user_info import username, password

DB_NAME = "sysut_test_db"

# Standard Flask configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@localhost/{DB_NAME}"
db = SQLAlchemy(app)

# Create database
create_db(username, password, DB_NAME)

# create all tables, columns and rows in database
db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Munchies!'


if __name__ == '__main__':
    app.run()
