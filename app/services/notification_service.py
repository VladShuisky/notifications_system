import asyncio
import logging
from typing import Iterable

from ..config import settings
from ..providers.base import NotificationProvider


logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self, providers: Iterable[NotificationProvider]):
        self.providers = list(providers)

    async def _send_with_retry(self, provider: NotificationProvider, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None) -> None:
        attempts = settings.provider_retry_attempts
        delay_ms = settings.provider_retry_initial_delay_ms
        for attempt in range(1, attempts + 1):
            try:
                await provider.send(message=message, email=email, phone=phone, telegram_chat_id=telegram_chat_id)
                return
            except Exception as exc:  # noqa: BLE001 - log and retry
                logger.warning("Provider %s failed on attempt %s/%s: %s", provider.name, attempt, attempts, exc)
                if attempt == attempts:
                    raise
                await asyncio.sleep(max(0, delay_ms) / 1000.0)
                delay_ms = int(delay_ms * settings.provider_retry_backoff_multiplier)

    async def send_with_fallback(self, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None):
        last_error: Exception | None = None
        for provider in self.providers:
            try:
                await self._send_with_retry(provider, message=message, email=email, phone=phone, telegram_chat_id=telegram_chat_id)
                logger.info("Delivered via %s", provider.name)
                return provider.name
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                logger.info("Falling back from %s due to error: %s", provider.name, exc)
        if last_error is not None:
            raise last_error






