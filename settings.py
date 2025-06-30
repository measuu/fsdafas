import os

import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dotenv.load_dotenv()


class DatabaseConfig:
    DATABASE_NAME = os.getenv("DATABASE_NAME", "shoe_store")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    ROOT_DB_PASSWORD = os.getenv("DB_PASSWORD")
    ROOT_DB_USER = os.getenv("DB_USER", "postgres")

    SECRET_KEY = os.getenv("SECRET_KEY")

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    MAX_FORM_MEMORY_SIZE = 1024 * 1024  # 1MB
    MAX_FORM_PARTS = 500

    NAME_RESTAURNAT = "CS WIK"

    def uri_postgres(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@localhost:5432/{self.DATABASE_NAME}"

    def uri_sqlite(self):
        return f"sqlite:///{self.DATABASE_NAME}.db"


config = DatabaseConfig()

# Налаштування бази даних Postgres
engine = create_engine(config.uri_postgres(), echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    def create_db(self):
        self.metadata.create_all(engine)

    def drop_db(self):
        self.metadata.drop_all(engine)
