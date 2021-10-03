from django.urls import path

from . import views

urlpatterns = [
    path('', views.random_string, name='random_string')
]
