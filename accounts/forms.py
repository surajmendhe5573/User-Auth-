from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age= forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2']
