from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartapp_cart, name='cartapp_cart'),
    path('order/', views.cartapp_order, name='cartapp_order')
]