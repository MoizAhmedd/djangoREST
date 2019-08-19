from django.db import models

# Create your models here.
class Songs(models.Model):
    song = models.TextField()
    artist = models.TextField()
    def __str__(self):
        return "{} by {}".format(self.song,self.artist) 