from django.urls import path
from . import views

app_name = 'maquiadores'

urlpatterns = [
    path('', views.lista_maquiadores, name='lista_maquiadores'),
    path('form/', views.novo_Maquiador, name='novo_Maquiador'),
    path('<int:pk>/form/', views.editar_Maquiador, name='editar_Maquiador'),
    path('<int:pk>/delete/', views.deletar_Maquiador, name='deletar_Maquiador'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
