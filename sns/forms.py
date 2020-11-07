from sns.models import Friend
from django import forms
from django.forms.widgets import TextInput


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail','gender','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False,
        widget=forms.TextInput(attrs={'class':'form-control'}))