import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/data/db.sqlite3"
    SECRET_KEY: str = "SECRETKEY"
    ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


# Получаем параметры для загрузки переменных среды
settings = Settings()
database_url = settings.DB_URL
