import logging
from fastapi import FastAPI, HTTPException

from .config import settings
from .schemas import NotificationRequest, NotificationResponse
from .providers import EmailProvider, SMSProvider, TelegramProvider
from .services.notification_service import NotificationService


logging.basicConfig(level=logging.INFO)
app = FastAPI(title=settings.app_name)


def build_providers(request: NotificationRequest):
    providers = []
    channels = set(request.channels)
    if "email" in channels and request.email:
        providers.append(EmailProvider())
    if "sms" in channels and request.phone:
        providers.append(SMSProvider())
    if "telegram" in channels and request.telegram_chat_id:
        providers.append(TelegramProvider())
    return providers


@app.post("/notify", response_model=NotificationResponse)
async def notify(payload: NotificationRequest):
    providers = build_providers(payload)
    if not providers:
        raise HTTPException(status_code=400, detail="No valid channels or recipients provided")

    service = NotificationService(providers)
    try:
        channel = await service.send_with_fallback(
            message=payload.message,
            email=payload.email,
            phone=payload.phone,
            telegram_chat_id=payload.telegram_chat_id,
        )
        return NotificationResponse(delivered_via=channel, status="delivered")
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=str(exc)) from exc






