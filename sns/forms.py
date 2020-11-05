from django import forms
from django.forms.widgets import TextInput


class SnsForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-contorl'}))
    mail = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class:':'form-control'}))