from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=50)
    text = models.TextField(max_length=140, blank=False)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-time',)
    
