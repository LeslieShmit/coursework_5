from django.contrib import admin

from habbits.models import Habbit


@admin.register(Habbit)
class HabbitAdmin(admin.ModelAdmin):
    """Класс описания административной панели"""

    list_display = ("id", "action", "is_pleasant", "owner", "is_published")
    list_filter = ("action", "is_pleasant", "owner")
    search_fields = ("action", "is_pleasant", "owner")