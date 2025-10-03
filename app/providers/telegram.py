import asyncio
import logging
from .base import NotificationProvider
from ..config import settings


logger = logging.getLogger(__name__)


class TelegramProvider(NotificationProvider):
    name = "telegram"

    async def send(self, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None) -> None:
        if not settings.telegram_enabled:
            raise RuntimeError("Telegram provider disabled")
        if not telegram_chat_id:
            raise ValueError("Telegram chat id not provided")

        # Placeholder: симуляция отправки сообщения с помощью asyncio.sleep
        await asyncio.sleep(0.05)
        logger.info("Telegram message sent to chat %s: %s", telegram_chat_id, message)






