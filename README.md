## Notification Service (FastAPI)

### Quickstart
1. Создайте и активируйте виртуальное окружение, например с помощью команды python -m venv myvenv
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. скопируйте переменные окружения:
```bash
copy .env.example .env
```
4. Запустите сервер:
```bash
uvicorn app.main:app --reload --port 8000
```

### Пример запроса с помощью curl
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

### Замечания
- Отдельные каналы(СМС, телеграм, эл-почта) "мокированы". При необходимости можно их реализовать отдельно, с помощью интеграций с апи, SDK и так далее.






