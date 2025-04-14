from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),  # Alterado de 'views.index' para 'views.device_list'
    path('create/', views.device_create, name='device_create'),
    path('update/<int:pk>/', views.device_update, name='device_update'),
    path('delete/<int:pk>/', views.device_delete, name='device_delete'),
]