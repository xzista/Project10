from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомный пользователь с расширенными полями профиля (телефон и дата рождения).
    """

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        error_messages={
            "unique": "Пользователь с таким email уже существует.",
        },
    )
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-created_at",)

    def __str__(self):
        return self.username
