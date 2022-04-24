from django.forms import ModelForm, Textarea
from .models import Message
from django import forms
from django.utils import timezone


class MessageSaveForm(ModelForm):

    time = forms.DateTimeField(
        widget=forms.HiddenInput(), initial=timezone.now())
    username = forms.CharField(widget=forms.HiddenInput(), initial="prueba")
    userid = forms.CharField(widget=forms.HiddenInput(), initial="prueba")
    message_id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            'text': Textarea(attrs={'class': 'form', 'cols': 80, 'rows': 3}),
        }
        exclude = ["userid", "username", "time"]
