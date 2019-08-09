from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()

# The following ensures the object does not only have an object name but is
# defined by its title:
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
