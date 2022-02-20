from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


# Create database
def create_db(username, password, DB_NAME):
    engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)
    print(f"Database {DB_NAME} already exists:", database_exists(engine.url))
