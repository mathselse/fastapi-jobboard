import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(env_path)

class Settings:
    PROJECT_TITLE: str = 'JobBoard'
    PROJECT_VERSION: str = '1.0.0'

    PG_USERNAME: str = os.getenv('PG_USERNAME')
    PG_PASSWORD: str = os.getenv('PG_PASSWORd')
    PG_SERVER: str = os.getenv('PG_SERVER', 'localhost')
    PG_PORT: str = os.getenv('PG_PORT', 5432)
    PG_DB: str = os.getenv('PG_DB', 'db_jobboard')
    DB_URL: str = f'postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_SERVER}:{PG_PORT}/{PG_DB}'

settings = Settings()
