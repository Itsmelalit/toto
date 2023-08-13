from . import views
from django.urls import path
from django.template import loader

urlpatterns = [
    path('',views.home),
]