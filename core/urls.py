from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/<int:id>/', views.addProduct, name='add-product'),
    path('add-collection/', views.addCollection, name='add-collection'),
    path('collections/', views.collections, name='collections'),
    path('collection/<int:id>/', views.collection, name='collection'),
]