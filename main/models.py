from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # O model User vem por dafault no django

class ToDoList(models.Model):            # para criar um model, criamos uma classe que herdará models.Model do próprio django
    name = models.CharField(max_length=200)  # cada variáverl será o nome da coluna com os atributos que ela deve ter
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  # para quando quisermos printar essa tabela, receberemos informação em forma de string
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # é assim que se estabelece uma chave estrangeira
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
