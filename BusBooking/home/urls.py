from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.Bookings, name='booking'),
    path('booking/pay/', views.AmountPay, name='pay_amount'),
]