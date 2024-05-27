from rest_framework.urls import path

from . import views

urlpatterns = [
    path('get_plans/', views.get_plans),
    path('get_zarinpal_url/', views.get_zarinpal_url),
    path('send_request/', views.send_request),
    path('verify/', views.verify),
    path('add_bazar_myket_order/', views.add_bazar_myket_order),
    path('get_transactions/', views.get_transactions),

]
