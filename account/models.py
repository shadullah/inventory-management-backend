from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    img=models.URLField(default="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

    def __str__(self) -> str:
        return self.user.username
