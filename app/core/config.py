from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Compliance Engine"
    OPENROUTER_API_KEY: str 
    QDRANT_PATH: str = "./qdrant_data"
    COLLECTION_NAME: str = "compliance_index"
    ENV: str = "dev"

    class Config:
        env_file = ".env"


settings = Settings()
