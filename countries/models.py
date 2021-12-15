from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    deleted = models.BooleanField(default=False)