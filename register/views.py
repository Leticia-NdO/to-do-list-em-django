from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)  # se a página for acessada por uma requisição post, popula o formulário com as informações passadas
        if form.is_valid():
            form.save()
            return redirect('/create')

        
    else:
        form = RegisterForm()  # Se a página for acessada por uma requisição get, o formulário aparecerá vazio

    return render(response, "register/register.html", {"form": form})
