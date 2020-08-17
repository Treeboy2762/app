from django.db import models

# Create your models here.

class Movie(models.Model):
  id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=140)
  genre = models.CharField(max_length=140)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']
