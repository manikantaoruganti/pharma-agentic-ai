import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    openai_api_key: Optional[str] = os.getenv('OPENAI_API_KEY')
    anthropic_api_key: Optional[str] = os.getenv('ANTHROPIC_API_KEY')
    iqvia_api_key: Optional[str] = os.getenv('IQVIA_API_KEY')
    postgres_url: Optional[str] = os.getenv('POSTGRES_URL')
    mongo_url: Optional[str] = os.getenv('MONGO_URL')
    redis_url: str = os.getenv('REDIS_URL', 'redis://localhost:6379')
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    environment: str = os.getenv('ENVIRONMENT', 'development')
    fastapi_port: int = int(os.getenv('FASTAPI_PORT', '8000'))
    max_parallel_agents: int = 5
    agent_timeout: int = 300
    max_retries: int = 3
    llm_model: str = 'gpt-4'
    temperature: float = 0.7
    max_tokens: int = 2000
    
    class Config:
        env_file = '.env'
        case_sensitive = False

settings = Settings()
