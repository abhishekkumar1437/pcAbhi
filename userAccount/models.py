from django.contrib.auth.models import User
from django.db import models

class signup_user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.TextField()
    cpassword=models.TextField()

