from re import S
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import ToDoList, Item
from main.forms import CreateNewList
from django.contrib.auth.models import User


def index(response, id):
    t = ToDoList.objects.get(id=id)
    s = t.item_set.all()
    if response.method == "POST":  # se a requisição for POST
        print(response.POST)
        if response.POST.get("save"):  # o nome do botão
            for item in t.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":  # o nome de cada item é c+id do item
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()
        
        elif response.POST.get("newItem"):  # se o response.POST tiver um valor newItem:
            txt = response.POST.get("novo")  # txt recebe o valor que foi digitado no input "novo"

            if len(txt) >= 2:  # uma verificação simples
                t.item_set.create(text = txt, complete = False)  # criação do novo item
                return HttpResponseRedirect("/%i" % t.id)  # recarregar a página e mostrar o novo item
            else:
                print('input inválido')
    return render(response, "main/home.html", {"items": s, "name": t.name, "t": t}) # passamos variáveis pelo dicionário. 
    # o texto em HttpResponse é html, se quiser colocar uma tag é possível, como '<h1>olá</h1>'

def home(response):
    username = response.user
    if username.is_authenticated:  # verifica se o usuário tá autentificado
        user = User.objects.get(username=username)
        t = ToDoList.objects.filter(user_id=user.id)
        return render(response, "main/lista.html", {"t": t}) # sendo main o nome da pasta criada dentro de templates*    
    else:   
       return HttpResponseRedirect("/login")
        
    

def create(response):
    user = response.user  # response.user contém o usuário
    # print(user)
    if response.method == "POST":
        form = CreateNewList(response.POST)  # assim, pegamos todas as informações do formulário em forma de um dicionário

        if form.is_valid():  # podemos usar o método is_valid() porque o formulário que criamos em forms.py é herdado de outra classe do django forms.Form
            n = form.cleaned_data["name"]  # cleaned_data só limpa os dados da criptografia, e lemos os dados contidos no campo "name"
            t = user.todolist_set.create(name=n)
            # t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" % t.id)
        

    else:
        form = CreateNewList
    return render(response, "main/create.html", {"form": form})
