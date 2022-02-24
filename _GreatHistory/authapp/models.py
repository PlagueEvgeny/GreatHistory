from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserProfile(AbstractUser):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9, 15}$',
        message=('Введите номер до 15 знаков')
    )
    phone_number = models.CharField(validators=[phone_validator], max_length=17, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.username}'

    def restore(self):
        self.is_active = True
        self.save()

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
