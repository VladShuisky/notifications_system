from typing import Literal, Optional
from pydantic import BaseModel, Field, EmailStr


Channel = Literal["email", "sms", "telegram"]


class NotificationRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    channels: list[Channel] = Field(default_factory=lambda: ["email", "sms", "telegram"])

    # Recipient fields
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, description="E.164 phone number")
    telegram_chat_id: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Hello from our notification service!",
                "channels": ["email", "sms", "telegram"],
                "email": "user@example.com",
                "phone": "+15551234567",
                "telegram_chat_id": "123456789",
            }
        }


class NotificationResponse(BaseModel):
    delivered_via: Optional[Channel] = None
    status: Literal["delivered", "failed"]
    error: Optional[str] = None






