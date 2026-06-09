"""Configuration management for ServerForge AI."""
import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field, field_validator


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Discord Configuration
    discord_token: str = Field(..., alias="DISCORD_TOKEN")
    command_prefix: str = Field("sf!", alias="COMMAND_PREFIX")
    bot_owner_id: Optional[int] = Field(None, alias="BOT_OWNER_ID")

    # Database Configuration
    database_url: str = Field(..., alias="DATABASE_URL")
    database_pool_size: int = Field(20, alias="DATABASE_POOL_SIZE")
    database_max_overflow: int = Field(10, alias="DATABASE_MAX_OVERFLOW")

    # Redis Configuration
    redis_url: str = Field("redis://localhost:6379/0", alias="REDIS_URL")
    redis_pool_size: int = Field(10, alias="REDIS_POOL_SIZE")

    # API Configuration
    api_host: str = Field("0.0.0.0", alias="API_HOST")
    api_port: int = Field(8000, alias="API_PORT")
    api_debug: bool = Field(False, alias="API_DEBUG")
    api_secret_key: str = Field(..., alias="API_SECRET_KEY")

    # Bot Configuration
    bot_version: str = Field("1.0.0", alias="BOT_VERSION")
    default_cooldown: int = Field(3, alias="DEFAULT_COOLDOWN")

    # Logging Configuration
    log_level: str = Field("INFO", alias="LOG_LEVEL")
    log_file: str = Field("serverforge.log", alias="LOG_FILE")

    # Feature Flags
    enable_premium: bool = Field(True, alias="ENABLE_PREMIUM")
    enable_analytics: bool = Field(True, alias="ENABLE_ANALYTICS")
    enable_ai: bool = Field(True, alias="ENABLE_AI")

    # Localization
    default_language: str = Field("en", alias="DEFAULT_LANGUAGE")

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = False

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Validate database URL format."""
        if not v.startswith(("postgresql://", "postgresql+psycopg2://", "postgresql+asyncpg://")):
            raise ValueError("Database URL must start with postgresql://")
        return v

    @field_validator("redis_url")
    @classmethod
    def validate_redis_url(cls, v: str) -> str:
        """Validate Redis URL format."""
        if not v.startswith("redis://"):
            raise ValueError("Redis URL must start with redis://")
        return v


def get_settings() -> Settings:
    """Get application settings."""
    return Settings()
