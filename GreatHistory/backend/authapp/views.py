from django.contrib.auth.views import LoginView
from rest_framework.viewsets import ModelViewSet

from authapp.forms import LoginForm
from authapp.models import UserProfile
from authapp.serializers import UserProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authapp/login.html'
