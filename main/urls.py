from django.urls import path
from . import views  # importa tudo de views

urlpatterns = [  # a função path leva três argumentos: o primeiro é a rota, o segundo é o que deve ser executado nesse rota, e o terceiro é o nome dessa página
    path("<int:id>", views.index, name='index'),  # isso significa que um número inteiro será requisitado e irá ser buscado em views.index. Então views.index precisa de um parâmetro chamado id
    path("", views.home, name='home'),
    path("create/", views.create, name='create'),

]