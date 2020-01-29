from django import forms
from homes.models import kilidUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(label="Password", max_length=5)
    #
    #
    # class Meta:
    #     model = kilidUser
    #     fields = ("username", "password","phoneNum", "email","userLevel")
