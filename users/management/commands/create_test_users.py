from datetime import date

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

USERS = [
    {
        "username": "admin",
        "email": "admin@mail.ru",
        "password": "admin123",
        "birth_date": date(1990, 1, 1),
        "is_staff": True,
        "is_active": True,
        "is_superuser": True,
    },
    {
        "username": "user1",
        "email": "user1@mail.ru",
        "password": "user12345",
        "birth_date": date(1995, 5, 10),
        "is_staff": False,
        "is_active": True,
        "is_superuser": False,
    },
    {
        "username": "user2",
        "email": "user2@yandex.ru",
        "password": "user12345",
        "birth_date": date(1998, 3, 15),
        "is_staff": False,
        "is_active": True,
        "is_superuser": False,
    },
]


class Command(BaseCommand):
    help = "Создание тестовых пользователей"

    def handle(self, *args, **options):
        self.stdout.write("Создание тестовых пользователей\n")

        for data in USERS:
            user, created = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "birth_date": data["birth_date"],
                    "is_staff": data["is_staff"],
                    "is_active": data["is_active"],
                    "is_superuser": data["is_superuser"],
                },
            )

            if created:
                user.set_password(data["password"])
                user.save()
                status = self.style.SUCCESS("CREATED")
            else:
                status = self.style.WARNING("EXISTS")

            self.stdout.write(
                f"{status} "
                f"user='{user.username}', "
                f"email='{user.email}', "
                f"is_staff={user.is_staff}, "
                f"is_active={user.is_active}, "
                f"is_superuser={user.is_superuser}"
            )

        self.stdout.write(self.style.SUCCESS("\nПользователи созданы"))