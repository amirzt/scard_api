from rest_framework.urls import path

from . import views

urlpatterns = [
    path('users/', views.login),
    path('check_otp/', views.check_otp),
    path('shops/', views.get_shops),
    path('add_favorite/', views.add_favorite),
    path('offers/', views.get_offers),
    path('splash/', views.splash),
    path('get_home/', views.get_home),
]
