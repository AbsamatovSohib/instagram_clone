from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)

    REQUIRED_FIELDS = []

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
