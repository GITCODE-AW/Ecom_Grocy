from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.userapp_register, name='userapp_register'),
    path('login/', views.userapp_login, name='userapp_login'),
    path('account/', views.userapp_account, name='userapp_account'),
    path('logout/', views.userapp_logout, name='userapp_logout'),
    path('forgot/', views.userapp_forgot, name='userapp_forgot_password'),
    path('reset/<str:uuid>', views.userapp_reset, name='userapp_reset'),
    path('verify/<str:uuid>', views.userapp_verify, name='userapp_verify')
]