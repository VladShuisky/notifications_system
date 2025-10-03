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

        # Placeholder: simulate sending via SMTP or an email API
        # In a real implementation, integrate aiosmtplib or an email API client.
        await asyncio.sleep(0.05)
        logger.info("Email sent to %s: %s", email, message)






