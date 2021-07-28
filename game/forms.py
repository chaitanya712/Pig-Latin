from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=8,widget=forms.PasswordInput)
    