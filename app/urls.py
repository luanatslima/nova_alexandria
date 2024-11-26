from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('meus-materiais', views.meus_materiais, name="meus_materiais"),
    path('area_usuario', views.area_usuario, name="area_usuario"),
    path('sobre_nos', views.sobre_nos, name="sobre_nos"),
    path('configuracoes', views.configuracoes, name="configuracoes"),
]