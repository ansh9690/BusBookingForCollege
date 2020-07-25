from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.Bookings, name='booking'),
    path('pay-amount/', views.HandleRequest, name='handlerequest'),
    path('upload-file/', views.import_file, name='import_file'),
]