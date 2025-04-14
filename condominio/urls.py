from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import necessário para criar uma resposta simples

# Definição da função home
def home(request):
    return HttpResponse("Bem-vindo ao sistema de condomínio!")  # Página inicial simples

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', include('device_control.urls')),
    path('location/', include('location.urls')),
    path('events/', include('events.urls')),
    path('audit/', include('audit.urls')),
    path('', home, name='home'),  # Adicionada a rota para a página inicial
]