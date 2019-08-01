from django.db import models

class Command(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
