from django.contrib import admin
from lesson.models import LessonModel


@admin.register(LessonModel)
class LessonAdmin(admin.ModelAdmin):
    ...
