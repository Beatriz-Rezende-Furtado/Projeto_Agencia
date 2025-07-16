from django.urls import path
from . import views

app_name = 'modelos'

urlpatterns = [
    path('', views.lista_modelos, name='lista_modelos'),
    # path('novo/', views.novo_Modelo, name='novo_Modelo'),
    # path('<int:pk>/editar/', views.editar_Modelo, name='editar_Modelo'),
    path('<int:pk>/delete/', views.deletar_Modelo, name='deletar_Modelo'),
    path('form/', views.novo_Modelo, name='novo_Modelo'),
    path('<int:pk>/form/', views.editar_Modelo, name='editar_Modelo'),
    path('sucesso/', views.sucesso, name='sucesso'),
]

