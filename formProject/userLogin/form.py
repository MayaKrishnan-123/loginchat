

from django import forms
from .models import userlogin

class registrationform(forms.Form):
    first_name = forms.CharField(label="Enter first name",max_length=100)
    last_name = forms.CharField(label="Enter second name",max_length=50)
    username = forms.CharField(label="Enter the Username",max_length=20)
    password1= forms.CharField(widget=forms.PasswordInput,label="Enter your password",max_length=15)
    password2= forms.CharField(widget=forms.PasswordInput,label="confirm your password",max_length=15)

class loginform(forms.Form):
    username = forms.CharField(label="enter your username to login",max_length=20)
    password1=forms.CharField(widget=forms.PasswordInput,label="enter your password to login",max_length=20)

class Editform(forms.ModelForm):

    class Meta:
        model = userlogin
        fields = (
            'first_name',
            'last_name',
            'username'
        )

