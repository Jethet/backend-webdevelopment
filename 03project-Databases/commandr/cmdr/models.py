from django.db import models

class Command(models.Model):
    text = models.TextField()

# This gets the name of what is entered as 'Command' and shows it:

    def __str__(self):
        return self.text
