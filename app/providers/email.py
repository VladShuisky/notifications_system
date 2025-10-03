import asyncio
import logging
from .base import NotificationProvider
from ..config import settings


logger = logging.getLogger(__name__)


class EmailProvider(NotificationProvider):
    name = "email"

    async def send(self, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None) -> None:
        if not settings.email_enabled:
            raise RuntimeError("Email provider disabled")
        if not email:
            raise ValueError("Email recipient not provided")

        # Placeholder: симуляция отправки сообщения с помощью asyncio.sleep
        await asyncio.sleep(0.05)
        logger.info("Email sent to %s: %s", email, message)






