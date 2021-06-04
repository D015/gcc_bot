from os import environ

from gcc_app import settings


DB_USER = environ.get("DB_USER", settings.db_user)
DB_PASSWORD = environ.get("DB_PASSWORD", settings.db_password)
DB_HOST = environ.get("DB_HOST", settings.db_host)
DB_PORT = environ.get("DB_PORT", settings.db_port)
DB_NAME = environ.get("DB_NAME", settings.db_name)

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+asyncpg://" f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
ALEMBIC_SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://" f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


REDIS_HOST = environ.get("REDIS_HOST", settings.redis_host)
REDIS_PORT = environ.get("REDIS_PORT", settings.redis_port)
REDIS_PASSWORD = environ.get("REDIS_PASSWORD", settings.redis_password)
REDIS_DB_INDEX = environ.get("REDIS_DB_INDEX", settings.redis_db_index)

REDIS_URI = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "password": REDIS_PASSWORD,
    "db": REDIS_DB_INDEX,
}

TOKEN_BOT = settings.token_bot

EMAIL_GOOGLE_CALENDAR = settings.email_google_calendar

COMMAND_CREATE_EVENT = ("/create_event", "Создать событие")
COMMAND_HELP = ("/help", "Помощь")
COMMAND_START = ("/start", "Старт")
COMMAND_TEST = ("/test", "Тест")
