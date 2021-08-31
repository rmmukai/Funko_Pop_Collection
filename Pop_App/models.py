from django.db import models

class Pop_Entry(models.Model):
    character = models.CharField(max_length=30)
    series = models.CharField(max_length=50)
    series_number = models.IntegerField()
    special_edition = models.CharField(max_length=30)

