from celery import shared_task


@shared_task
def send_notification(lesson_name: str, student_id: int) -> None:
    """
    Отправка уведомлений студентам урока.

    Args:
        lesson_name: Название урока
        student_id: ID студента
    """
    print(f"Уведомление отправлено студенту {student_id} по уроку {lesson_name}")
