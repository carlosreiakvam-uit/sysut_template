from flask import Flask
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from db_user_info import username, password
from sqlalchemy_utils import database_exists, create_database

DB_NAME = "sysut_test_db"

# Create database
engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost/{DB_NAME}")
if not database_exists(engine.url):
    create_database(engine.url)
print(f"Database {DB_NAME} already exists:", database_exists(engine.url))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@localhost/{DB_NAME}"
db = SQLAlchemy(app)


@click.command(name='update_local_db')
@with_appcontext
def update_local_db():
    db.create_all()


app.cli.add_command(update_local_db)


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
