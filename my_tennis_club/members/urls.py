from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('hello/', views.members1, name='members1'),
    path('farm_production/',views.farmequipment, name="farm equipment"),
    path('farm_animals/',views.farmanimals, name="farm animals"),
    path('memberslist/', views.memberslist, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
