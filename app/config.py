from dotenv import load_dotenv
from pydantic_setting import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    google_client_id: str
    google_client_secret: str
    google_client_token: str
    database_url: str
    classifier_model: str = "openai: gpt-5-nano"
    agent_model: str = "openai: gpt-4o-mini"
    poll_interval_seconds: int = 60
    dashboard_username: str = "admin"
    dashboard_password: str = ""


settings = Settings()
