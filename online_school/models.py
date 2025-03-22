from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

NULLBLE = {"blank": True, "null": True}

class Сourse(models.Model):
    name = models.CharField(max_length=100, verbose_name="название курса")
    description = models.TextField(verbose_name="описание курса")
    preview = models.ImageField(upload_to="сourse/", verbose_name="превью", **NULLBLE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="сourse",
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
    link_video = models.CharField(max_length=100, verbose_name="ссылка на видео")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="lesson",
        verbose_name="создатель",
        **NULLBLE)
    сourse = models.ForeignKey(
        Сourse,
        on_delete=models.SET_NULL,
        related_name="lesson",
        verbose_name="курс",
        **NULLBLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
