from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017/"
    DB_NAME: str = "finanzas_db"
    FIREBASE_API_KEY: str
    FIREBASE_CREDENTIALS_PATH: str
    class Config:
        env_file = ".env"

settings = Settings()
