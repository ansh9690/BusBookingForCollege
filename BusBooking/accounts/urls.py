from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    # register / login / logout urls
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy(
        'accounts:password_change_done'), template_name='accounts/password_change_form.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),
]
