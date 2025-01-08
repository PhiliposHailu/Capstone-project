from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()

class UserRegisteration(CreateView):

    model = User
    form_class = CustomUserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):

    template_name = 'user/login.html'

class CustomLogoutView(LogoutView):

    template_name = 'user/logout.html'

class ProfileView(TemplateView):

    template_name = 'user/profile.html'

