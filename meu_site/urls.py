"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', rv.register, name='register'),
    path('', include('main.urls')),   # isso conecta a nossa aplicação (com os caminhos que definiremos em urls) ao projeto. Isso basicamente diz que se o usuário não digitar nenhum argumento, ele vai diretamente para a aplicação "main"
    path('', include("django.contrib.auth.urls"))  # ao conectar esse app built in do django à nossa aplicação, ele vai automaticamente procurar por um aquivo chamado login.html. Apesar das aspas estarem vazias, esse caminho é "login/"
    # além disso, assim que o usuário logar, o django vai, automaticamente, se redirecionar para accounts/profile. Para personalizar isso, em settings.py, no final da página, coloque LOGIN_REDIRECT_URL = "/", sendo entre aspas o caminho de redirecionamento após o login 
]
