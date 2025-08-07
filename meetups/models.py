from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')