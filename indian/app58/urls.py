# encoder/urls.py
from django.urls import path
from .views import encode_view

urlpatterns = [
    path('', encode_view, name='encode'),
]
