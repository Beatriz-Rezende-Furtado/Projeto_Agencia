from django.urls import path
from . import views

app_name = 'estilistas'

urlpatterns = [
    path('', views.lista_estilistas, name='lista_estilistas'),
    path('form/', views.novo_Estilista, name='novo_Estilista'),
    path('<int:pk>/form/', views.editar_Estilista, name='editar_Estilista'),
    path('<int:pk>/delete/', views.deletar_Estilista, name='deletar_Estilista'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
