from pydantic import BaseSettings


class Settings(BaseSettings):
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_BUCKET_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
