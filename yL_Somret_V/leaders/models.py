from django.contrib.auth.models import AbstractUser
from django.db import models

class leader(AbstractUser):
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.username
# Create your models here.
