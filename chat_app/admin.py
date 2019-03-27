from django.contrib import admin

from .models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Администрирование моделей комнат чата."""

    list_display = ('creator', 'get_participants', 'creation_date')
    filter_horizontal = ('participants', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Администрирование моделей комнат чата."""

    list_display = ('room', 'sender', 'dispatch_date')
