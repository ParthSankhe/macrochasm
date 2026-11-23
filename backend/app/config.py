from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App configuration, read from environment variables or a .env file."""

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    database_url: str = "postgresql+psycopg://macrochasm:macrochasm@localhost:5432/macrochasm"
    kroger_client_id: str = ""
    kroger_client_secret: str = ""


settings = Settings()
