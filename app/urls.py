from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('meus-materiais', views.meus_materiais, name="meus_materiais"),
]