from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str
    mongodb_uri: str
    mongodb_db: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
