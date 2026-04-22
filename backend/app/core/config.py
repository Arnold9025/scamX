from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/scamx"
    SECRET_KEY: str = "change-me"


settings = Settings()
