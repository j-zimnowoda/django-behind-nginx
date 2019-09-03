from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dummy_url', views.dummy_url, name='dummy_url'),
]
