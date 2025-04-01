from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import validate_youtube_link

NULLBLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="название курса")
    description = models.TextField(verbose_name="описание курса")
    preview = models.ImageField(upload_to="course/", verbose_name="превью", **NULLBLE)
    price_course = models.PositiveIntegerField(default=0, verbose_name="Цена за курс")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="course",
        verbose_name="создатель",
        **NULLBLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="название урока")
    description = models.TextField(verbose_name="описание урока")
    preview = models.ImageField(upload_to="lesson/", verbose_name="превью", **NULLBLE)
    link_video = models.URLField(verbose_name="ссылка на видео", **NULLBLE)
    price_lesson = models.PositiveIntegerField(default=0, verbose_name="Цена за урок")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="lesson",
        verbose_name="создатель",
        **NULLBLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="lesson",
        verbose_name="курс",
        **NULLBLE)

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        if self.link_video:
            validate_youtube_link(self.link_video)
        super().clean()

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ['id']


class Payments(models.Model):
    NOT_PAID = 'Не оплачено'
    CASH = 'Наличные'
    BANK_TRANSFER = 'Банковский перевод'
    PAYMENT_METHOD = [
        (NOT_PAID, 'Не оплачено'),
        (CASH, 'Наличные'),
        (BANK_TRANSFER, 'Банковский перевод'),
    ]

    method_payment = models.CharField(max_length=100, choices=PAYMENT_METHOD, default=NOT_PAID,
                                      verbose_name="способ оплаты")
    payment_amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    session_id = models.CharField(max_length=225, verbose_name="способ оплаты",**NULLBLE)
    session_link = models.URLField(max_length=400, verbose_name="ссылка на оплату",**NULLBLE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="payments",
        verbose_name="пользователь",
        **NULLBLE)
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="оплаченный курс",
        **NULLBLE)
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        related_name="payments",
        verbose_name="оплаченный урок",
        **NULLBLE)

    def __str__(self):
        return f"оплатил -{self.user} сумма оплаты - {self.payment_amount}"

    class Meta:
        verbose_name = "платёж"
        verbose_name_plural = "платежи"

class Subscription(models.Model):
    subscription_activated = models.BooleanField(default=False, verbose_name="подписка активирована")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="subscription",
        verbose_name="пользователь",
        **NULLBLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="subscription",
        verbose_name="курс",
        **NULLBLE)
