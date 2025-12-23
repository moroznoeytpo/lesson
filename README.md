# Урок

## Запуск через Docker
```bash
docker compose up -d
```

## Локальный запуск
```bash
python -m venv .vent # Создание виртуального окружения
source .venv/bin/activate # Активация окружения
pip install -r requirements.txt # Установка зависимостей

python manage.py runserver # Запуск Django приложения
brew services start rabbitmq # Запуск брокера (macOs)
celery -A lesson worker --loglevel=info # Запуск Celery
```

## Настройка проекта
Для корректной работы нужно в корне проекта создать .env файл
```bash
CELERY_BROKER_URL=amqp://user:password@rabbitmq:5672//
CELERY_RESULT_BACKEND=rpc://
```


# Первый студент
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
user = User.objects.create_user(
    username='guest',
    email='guest@example.com',
    password='guest',
    is_superuser=True,
    is_staff=True,
)
```

# Логика
При сохранении урока в БД проверяем его статус (Завершен) и запускаем процесс отправки уведомления (имитация).
