from django.db import models

# Create your models here.

# 1 to N with Meetup
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.address})'


# M to N with Meetup
class Participant(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    
    def __str__ (self):
        return f'{self.title} - {self.slug}'