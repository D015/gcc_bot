from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import Config

# todo add psycopg2
engine = create_engine(
    f'postgresql://{Config.SQLALCHEMY_DATABASE_URI}', echo=True)
base = declarative_base()