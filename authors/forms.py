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
        # mostra todos os campos, excluindo o que eu escolhi
        # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'The e-mail must be valid'
        }
        error_messages = {
            'username': {
                'required': 'This field must be not be empty',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your username here'
            }),  # referente ao que sera renderizado a tela
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here'
            })
        }
