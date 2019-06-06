from django.urls import path
from . import views

#Mapeando URL do polls de Hello World

urlpatterns = {
    path('', views.index, name='index')
}