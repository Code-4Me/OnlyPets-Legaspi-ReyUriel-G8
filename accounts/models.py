from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        PET_OWNER = 'pet_owner', 'Pet Owner'

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PET_OWNER
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username