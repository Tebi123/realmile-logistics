from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Realmile Logistics API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database config
    DATABASE_URL: str
    
    # Security config
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
