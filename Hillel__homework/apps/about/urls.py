from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whoami/', views.whoami, name='whoami'),
    path('source_code/', views.source_code, name='source_code')
]
