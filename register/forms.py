from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):  # isso signica que a classe RegisterForm terá também todas as propriedades de UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User  # o model de User vai ser salvo com o conteúdo do formulário
        fields = ("email", "username", "password1", "password2")  # precisamos informar quais os campos que queremos que sejam exibidos na tela, username, password1 e password2 são built-in do UserCreationForm
