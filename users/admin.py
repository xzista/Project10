from django.contrib import admin

from users.models import User


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("created_at",)
    list_display = ("username",)
