from flask import Flask
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from personal_db_user import username, password, db_name

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/{db_name}' \
    .format(username=username, password=password, db_name = db_name)
db = SQLAlchemy(app)


@click.command(name='create_db')
@with_appcontext
def create_db():
    db.create_all()


app.cli.add_command(create_db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username  # Test nyere syntaks her hihi


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Munchies!'


if __name__ == '__main__':
    app.run()
