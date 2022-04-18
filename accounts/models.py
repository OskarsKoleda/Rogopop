from django.db import models

from django.contrib.auth.models import (
    AbstractUser
)


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        # if self.first_name or self.last_name:
            # return f"{self.first_name} {self.last_name}"
        return self.user.username
