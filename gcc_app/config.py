from os import environ

from gcc_app import settings


class Config:

    DB_USER = environ.get('DB_USER', settings.db_user)
    DB_PASSWORD = environ.get('DB_PASSWORD', settings.db_password)
    DB_HOST = environ.get('DB_HOST', settings.db_host)
    DB_PORT = environ.get('DB_PORT', settings.db_port)
    DB_NAME = environ.get('DB_NAME', settings.db_name)

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://'
        f'{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    TOKEN_BOT = settings.token_bot


