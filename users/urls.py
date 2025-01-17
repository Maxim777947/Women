from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,\
      PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
      PasswordResetCompleteView


app_name = 'users'


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'), 
    #Через LogoutViev не получилось по причине что используется 5 джанго урок 9.4
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'), 
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'
        ), name='password_change_done'), 
    path('password-reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy('users:password_reset_done'),
        ), name='password_reset'), 
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
        ), name='password_reset_done'), 
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete'),
        ), name='password_reset_confirm'), 
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
        ), name='password_reset_complete'),
    path('register/', views.RegisterUser.as_view(), name='register'), 
    path('profile/', views.ProfileUser.as_view(), name='profile'), 
]

