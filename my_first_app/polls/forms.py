from django import forms

class Inputforms(forms.Form):
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=50)
