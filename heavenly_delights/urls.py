from django.urls import path
from . import views

#url config
urlpatterns = [
    path('index/', views.index),
]