from sns.models import Friend
from django import forms
from django.forms.widgets import TextInput


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail','gender','age','birthday']