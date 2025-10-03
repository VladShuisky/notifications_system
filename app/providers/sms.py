import asyncio
import logging
from .base import NotificationProvider
from ..config import settings


logger = logging.getLogger(__name__)


class SMSProvider(NotificationProvider):
    name = "sms"

    async def send(self, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None) -> None:
        if not settings.sms_enabled:
            raise RuntimeError("SMS provider disabled")
        if not phone:
            raise ValueError("Phone recipient not provided")

        # Placeholder: simulate sending via SMS provider (Twilio, etc.)
        await asyncio.sleep(0.05)
        logger.info("SMS sent to %s: %s", phone, message)






