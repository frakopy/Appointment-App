from django.urls import path
from .views import CustomLoginView, CustomLogoutView, HomeView, SignupView

urlpatterns = [
    path("auth/login/", CustomLoginView.as_view(), name="login"),
    path("auth/logout/", CustomLogoutView.as_view(), name="logout"),
    path("auth/signup/", SignupView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home"),
]
