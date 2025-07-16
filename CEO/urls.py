from django.urls import path
from . import views

app_name = 'CEO'

urlpatterns = [
    path('', views.Big_Boss, name='Big_Boss'),
    path('form/', views.editar_ceo, name='editar_ceo'),
]