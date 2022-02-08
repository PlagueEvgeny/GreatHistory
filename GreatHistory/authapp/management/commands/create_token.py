from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand
from authapp.models import UserProfile
from rest_framework import authentication


class TokenAuthentication(authentication.TokenAuthentication):
    authentication.TokenAuthentication.keyword = 'Bearer'


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        num = 0
        for user in UserProfile.objects.all():
            token = Token.objects.create(user=user)
            print(user, token.key)
            num += 1
        print(f"Finish {num}")
