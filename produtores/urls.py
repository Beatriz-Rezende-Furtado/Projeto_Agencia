from django.urls import path
from . import views

app_name = 'produtores'

urlpatterns = [
    path('', views.lista_produtores, name='lista_produtores'),
    path('form/', views.novo_Produtor, name='novo_Produtor'),
    path('<int:pk>/form/', views.editar_Produtor, name='editar_Produtor'),
    path('<int:pk>/delete/', views.deletar_Produtor, name='deletar_Produtor'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
