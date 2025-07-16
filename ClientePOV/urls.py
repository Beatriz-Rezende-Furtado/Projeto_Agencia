from django.urls import path
from . import views

app_name = 'clientePOV'

urlpatterns = [
    path('', views.home, name='home'),  
]