import re
from django.core.exceptions import ValidationError

ALLOWED_DOMAINS = ("mail.ru", "yandex.ru")

def validate_password(password: str):
    if len(password) < 8:
        raise ValidationError("Пароль должен быть не менее 8 символов")
    if not re.search(r"\d", password):
        raise ValidationError("Пароль должен содержать цифры")

def validate_email(email: str):
    domain = email.split("@")[-1]
    if domain not in ALLOWED_DOMAINS:
        raise ValidationError("Разрешены только mail.ru и yandex.ru")