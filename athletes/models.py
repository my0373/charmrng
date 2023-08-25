from django.db import models

class Athlete(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    photo_permission = models.BooleanField()
    disability_class = models.CharField(max_length=3)
