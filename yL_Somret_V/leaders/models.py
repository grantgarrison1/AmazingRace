from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now



class Leader(AbstractUser):
    # Removed user field since it’s not necessary
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Race(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Zone(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="zones")
    number = models.IntegerField()

    def __str__(self):
        return f"Zone {self.number} - {self.race.name}"

class Riddle(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="riddles")
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Riddle in {self.zone} - Q: {self.question}"

