from celery import shared_task
from django.core.mail import send_mail


from config.settings import EMAIL_HOST_USER
from online_school.models import Subscription


@shared_task
def mail_update_course_info(course_id):
    """Отправка сообщения об обновлении курса по подписке"""
    subscription_course = Subscription.objects.filter(course=course_id)
    print(f"Найдено {len(subscription_course)} подписок на курс {course_id}")
    for subscription in subscription_course:
        print(f"Отправка электронного письма на {subscription.user.email}")
        subject = "Обновление материалов курса"
        message = f'Курс {subscription.course.name} был обновлен.'
        from_email = EMAIL_HOST_USER
        recipient_list = [subscription.user.email]
        print(subject)
        print(message)
        print(from_email)
        print(recipient_list)
        fail_silently = False
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently
        )


@shared_task
def test_calery():
    print("Работает!!!")
