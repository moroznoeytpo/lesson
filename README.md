# Урок

## Запуск через Docker
```bash
docker compose up -d
```

## Локальный запуск
```bash
python manage.py runserver # Запуск Django приложения
brew services start rabbitmq # Запуск брокера
celery -A lesson worker --loglevel=info # Запуск Celery 
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
При сохранении урока в БД проверяем его статус (Завершен) и запускаем процесс отправки уведомления (имитация)