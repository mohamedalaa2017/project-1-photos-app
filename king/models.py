from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError



from datetime import datetime
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_response")
    title = models.CharField(max_length=64)
    describe = models.TextField()
    image = models.ImageField(upload_to="photos/20%y/%m/%d")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']






class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='depurtures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    during = models.IntegerField()

    def clean(self):
        if self.origin == self.destination:
            raise ValidationError("origin city can't be the destinaiton city ")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
