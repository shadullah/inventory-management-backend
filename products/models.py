from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=1000)
    description= models.TextField(max_length=10000)
    quantity= models.IntegerField(default=1)
    price=models.FloatField()
    image = models.URLField(default="https://assets.thehansindia.com/h-upload/2022/07/18/1303611-pro.webp")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name