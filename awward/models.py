from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, unique=True)
    bio = models.TextField(null=True)
    profile_pic = CloudinaryField('images')

class Project(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250)
    repo_link = models.CharField(max_length=500)
    live_link = models.CharField(max_length=500, blank=True)
    image = CloudinaryField('images', null=True)