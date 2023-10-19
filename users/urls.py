from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("profile/", view=views.profile, name="profile"),
    path("register/", view=views.register_user, name="register"),
    path("login/", view=auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("", view=views.home, name="home")
]
