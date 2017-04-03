from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class PortalForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','father_name','mother_name','registration_no','dept','semester','branch','thumbnail')
