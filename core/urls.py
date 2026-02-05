from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/<int:id>/', views.addProduct, name='add-product'),
    path('phone-info/<int:id>/', views.phoneDetails, name='phone-info'),
    path('product-details/<int:id>/', views.product_details, name='product-details'),
    path('edit-details/<int:id>', views.editProductDetails, name='edit-details'),
    path('edit-details1/<int:id>', views.editProductDetails1, name='edit-details1'),
    path('delete/<int:id>/', views.deleteProduct, name='delete'),
    path('add-collection/', views.addCollection, name='add-collection'),
    path('collections/', views.collections, name='collections'),
    path('collection/<int:id>/', views.collection, name='collection'),
]