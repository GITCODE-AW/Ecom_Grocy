from django.urls import path
from sellerapp import views

urlpatterns = [
    path('register/', views.seller_register, name='sellerapp_register'),
    path('pannel/', views.seller_panel, name='sellerapp_panel'),
    path('products/', views.seller_products, name='sellerapp_products')
]