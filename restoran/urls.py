from django.urls import path
from . import views

urlpatterns = [
    path('restoran/', views.restoran, name='restoran'),
]