from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField( required=True)
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)

    class Meta:
        model = User
        fields = ["first_name","last_name", "username", "email", "phone", "password1", "password2"]
