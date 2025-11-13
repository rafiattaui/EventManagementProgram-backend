from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

config_dir = Path(__file__).resolve().parent.parent.parent
print(config_dir)


class Settings(BaseSettings):
    DATABASE_URL: str

    # TODO - Fix .env not getting read
    app_name: str = "Event Management System API"
    model_config = SettingsConfigDict(
        env_file=config_dir / ".env", env_file_encoding="utf-8"
    )
