from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ("ерунда", "глупость", "чепуха")


def validate_author_age(user):
    if not user.birth_date:
        raise ValidationError("Дата рождения не указана.")
    age = relativedelta(date.today(), user.birth_date).years
    if age < 18:
        raise ValidationError("Автору должно быть не менее 18 лет.")


def validate_post_title(title):
    for word in FORBIDDEN_WORDS:
        if word in title.lower():
            raise ValidationError(f"Запрещенное слово: {word}")
