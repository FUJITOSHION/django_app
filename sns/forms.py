from django import forms


class SnsForm(forms.Form):
    data = [
        ('one', 'item1'),
        ('two', 'item2'),
        ('three', 'item3'),
    ]
    check = forms.ChoiceField(label='ratio',choices=data, widget=forms.RadioSelect())
    # name = forms.CharField(label='name')
    # mail = forms.CharField(label='mail')
    # age = forms.IntegerField(label='age')