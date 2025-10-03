## Notification Service (FastAPI)

### Features
- Email, SMS, Telegram providers (pluggable)
- Fallback with retries and exponential backoff
- Config via environment variables

### Quickstart
1. Create and activate a virtualenv (recommended).
2. Install deps:
```bash
pip install -r requirements.txt
```
3. Copy env and edit values:
```bash
copy .env.example .env
```
4. Run server:
```bash
uvicorn app.main:app --reload --port 8000
```

### Request example
```bash
curl -X POST http://localhost:8000/notify \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello!",
    "channels": ["email", "sms", "telegram"],
    "email": "user@example.com",
    "phone": "+15551234567",
    "telegram_chat_id": "123456789"
  }'
```

### Notes
- Providers are mocked to simulate delivery. Integrate real SMTP/SMS/Telegram SDKs where needed.
- Configure retries via `provider_retry_*` settings in `.env`.






