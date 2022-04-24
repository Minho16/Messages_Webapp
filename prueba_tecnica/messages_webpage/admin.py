from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User ID',          {'fields': ['userid']}),
        ('Username',          {'fields': ['username']}),
        ('Date information', {'fields': ['time']}),
        ('Message', {'fields': ['text']}),
    ]

    list_display = ('message_id', 'username', 'time', 'text')


admin.site.register(Message, MessageAdmin)
