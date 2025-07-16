from django.urls import path
from . import views

app_name = 'cabeleireiros'

urlpatterns = [
    path('', views.lista_cabeleireiros, name='lista_cabeleireiros'),
    path('<int:pk>/delete/', views.deletar_Cabeleireiro, name='deletar_Cabeleireiro'),
    path('form/', views.novo_Cabeleireiro, name='novo_Cabeleireiro'),
    path('<int:pk>/form/', views.editar_Cabeleireiro, name='editar_Cabeleireiro'),
    path('sucesso/', views.sucesso, name='sucesso'),
]




