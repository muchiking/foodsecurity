from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.members, name='members'),
    path('hello/', views.members1, name='members1'),
]