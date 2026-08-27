from django import forms

# from django.forms import form
# Default Form
# from django.forms import ModelForm

from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        # Class to pass META DATA To Forms.
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
