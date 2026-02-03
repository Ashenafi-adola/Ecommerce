from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout')
]