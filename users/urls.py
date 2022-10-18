from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('signin/', views.Signin.as_view(), name="signin"),
    path('signup/', views.Signup.as_view() , name="signup"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('password_reset/', views.PasswordReset.as_view(), name="password_reset"),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/', views.Reset.as_view(), name="password_reset_confirm"),
    path('accounts/reset/done/', views.ResetDone.as_view(), name="password_reset_complete"),
]
