from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('signup/', views.signup, name="users-sign-up"),
    path('login/', auth_view.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="users/logout.html"), name="users-logout"),


]
