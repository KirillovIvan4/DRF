from celery import shared_task
from datetime import timedelta
from django.utils import timezone


from users.models import User


@shared_task
def check_user_is_active():
    # Получаем текущую дату и время
    current_date = timezone.now()
    print(f"Текущая дата: {current_date}")

    # Вычисляем дату месяц назад
    one_month_ago = current_date - timedelta(days=30)

    # Фильтруем активных пользователей, которые не заходили последний месяц
    inactive_users = User.objects.filter(
        is_active=True,
        last_login__lt=one_month_ago  # last_login раньше чем месяц назад
    )
    for inactive_user in inactive_users:
        inactive_user.is_active = False
        inactive_user.save()
        print(f'Пользователь - {inactive_user} неактивен более месяца')
