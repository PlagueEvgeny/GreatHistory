import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from authapp.forms import LoginForm, RegisterForm
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet
from authapp.models import UserProfile
from authapp.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authapp/login.html'


class Logout(LogoutView):
    template_name = 'authapp/logout.html'
    success_url = reverse_lazy('auth:login')


class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('auth:login')
    template_name = 'authapp/register.html'
