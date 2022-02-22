from django.urls import path, include
import authapp.views as authapp
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.Login.as_view(), name='login'),
    path('logout/', authapp.Logout.as_view(), name='logout'),
    path('register/', authapp.Register.as_view(), name='register'),
]
