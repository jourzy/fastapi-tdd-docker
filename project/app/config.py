import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)

@lru_cache(maxsize=18)
def get_settings() -> BaseSettings:
    log.info("loading config settings from the environment....")
    return Settings()