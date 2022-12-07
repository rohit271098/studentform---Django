from django.db import models

# Create your models here.

class Contact(models.Model):                # using postgresql model
    usn = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, default='')
    sem = models.IntegerField(default='')
    phone = models.IntegerField(default='')
    email = models.EmailField(default='')

    def __str__(self) -> str:
        return self.name

