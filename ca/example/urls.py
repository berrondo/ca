from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('send', views.send, name='send'),
    path('process', views.process, name='process'),
]