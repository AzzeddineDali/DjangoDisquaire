from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='album_pics')
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)


class Booking(models.Model):
    contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
