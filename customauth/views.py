from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import SignupForm 


class HomeView(TemplateView):
    template_name = "customauth/home.html"


class CustomLoginView(LoginView):
    template_name = "customauth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("set_appointment")

class CustomLogoutView(LogoutView):
    next_page = 'home'


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "customauth/signup.html"

    def get_success_url(self):
        return reverse_lazy('login') + '?registered'
