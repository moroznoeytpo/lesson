from lesson.tasks import send_notification as task

def send_notification(lesson) -> None:
    """Отправка уведомлений студентам."""
    for student in lesson.students.all():
        task.delay(lesson_name=lesson.name, student_id=student.id)
