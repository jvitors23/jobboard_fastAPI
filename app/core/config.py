import os


class Settings:
    PROJECT_TITLE: str = 'Jobboard'
    PROJECT_VERSION: str = '0.1.0'
    DB_USER = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT', 5432)
    DB_PASS = os.getenv('DB_PASS')
    DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/' + \
        DB_NAME


settings = Settings()
