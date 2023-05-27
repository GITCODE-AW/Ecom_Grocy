from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_home, name='product_home'),
    path('<int:product_id>/', views.product_specific, name='product_specific')
]