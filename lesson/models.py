from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from lesson.services import send_notification
from django.db import transaction


class LessonModel(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 1, 'Черновик'
        PUBLISHED = 2, 'Опубликован'
        FINISHED = 3, 'Завершен'

    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)

    students = models.ManyToManyField(AUTH_USER_MODEL, related_name='students')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self) -> str:
        """Название урока"""
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Отслеживаем завершение урока
        if self.status == self.Status.FINISHED:
            # Ожидаем завершение транзакции
            transaction.on_commit(lambda: send_notification(lesson=self))
