from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):


    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending approval"
        ACTIVE =  "ACTIVE", "Active"


    username = None

    email = models.EmailField(unique = True)

    full_name = models.CharField(max_length = 255, blank = True)
    company = models.CharField(max_length = 255, blank = True)
    status = models.CharField(max_length = 16, choices=Status.choices, default = Status.PENDING)

    created_at = models.DateTimeField(auto_now_add = True)
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    