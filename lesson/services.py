def send_notification(lesson) -> None:
    """Отправка уведомлений студентам."""
    for student in lesson.students.all():
        send_notification.delay(lesson_name=lesson.name, student_id=student.id)
