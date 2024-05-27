from rest_framework.urls import path

from . import views

urlpatterns = [
    path('articles/', views.get_articles),

]
