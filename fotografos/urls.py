from django.urls import path
from . import views

app_name = 'fotografos'

urlpatterns = [
    path('', views.lista_fotografos, name='lista_fotografos'),
    path('form/', views.novo_Fotografo, name='novo_Fotografo'),
    path('<int:pk>/form/', views.editar_Fotografo, name='editar_Fotografo'),
    path('<int:pk>/delete/', views.deletar_Fotografo, name='deletar_Fotografo'),
    path('sucesso/', views.sucesso, name='sucesso'),
]


