from django import forms


class CreateForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
