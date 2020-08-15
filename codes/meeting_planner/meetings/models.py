from django.db import models


# import time for default values for start_time
from datetime import time


# Create your models here.

class Meeting (models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField() 
    start_time = models.TimeField(default = time(9))
    duration = models.IntegerField(default=1)


