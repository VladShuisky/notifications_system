from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # General
    app_name: str = Field(default="Notification Service")
    environment: str = Field(default="dev")

    # Retry / timeouts
    provider_retry_attempts: int = Field(default=3)
    provider_retry_initial_delay_ms: int = Field(default=200)
    provider_retry_backoff_multiplier: float = Field(default=2.0)

    # Email
    email_enabled: bool = Field(default=True)
    smtp_host: str | None = Field(default=None)
    smtp_port: int | None = Field(default=None)
    smtp_username: str | None = Field(default=None)
    smtp_password: str | None = Field(default=None)
    smtp_from_email: str | None = Field(default=None)

    # SMS (placeholder for an external provider)
    sms_enabled: bool = Field(default=True)
    sms_api_key: str | None = Field(default=None)
    sms_sender_id: str | None = Field(default=None)

    # Telegram
    telegram_enabled: bool = Field(default=True)
    telegram_bot_token: str | None = Field(default=None)

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()






