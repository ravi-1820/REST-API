from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)

    def __str__(self):
        return self.name
