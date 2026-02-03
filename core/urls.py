from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-Product/', views.addProduct, name='add-product'),
    path('add-collection/', views.addCollection, name='add-collection')
]