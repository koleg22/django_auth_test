
# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальный email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Необязательный телефон

    USERNAME_FIELD = 'email'  # Теперь вход по email
    REQUIRED_FIELDS = ['username']  # username остаётся обязательным