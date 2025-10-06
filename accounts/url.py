from django.urls import path
from .views import *
from . import views

from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/", create_user.as_view(), name="register"),
    path("login/", login_user.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    
    path("profile/<int:pk>/", profile.as_view(), name="profile"),
    path("update_profile/<int:pk>/", update_profile.as_view(), name="update_profile"),
   
   
    path("change_password/", ChangePasswordView.as_view(), name="change_password"), 
    
    
    path('reset_password/', MyPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    
]

