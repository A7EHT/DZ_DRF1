from idlelib.colorizer import make_pat

from django.db import models

class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/course_preview",
        blank=True,
        null=True,
        verbose_name="Превью курса",
        help_text="Загрузите превью курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    preview = models.ImageField(
        upload_to="materials/lesson_preview",
        blank=True,
        null=True,
        verbose_name="Превью урока",
        help_text="Загрузите превью урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    link_to_video = ...


    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"