from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("created_at",)
    list_display = ("title", "author_link", "created_at")

    def author_link(self, obj):
        url = reverse(
            "admin:users_user_change",
            args=[obj.author.id]
        )
        return format_html('<a href="{}">{}</a>', url, obj.author)

    author_link.short_description = "Автор"