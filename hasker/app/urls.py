from django.urls import path

from .views import ask_view

urlpatterns = [
    path('', ask_view, name='index'),
]
