from django.db import models

# import time for default values for start_time
from datetime import time


# Create your models here.

# Task:
# add a Model class called Room
# To represent a meeting room
# A room has a name, floor number, room numer

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField(default=101)

    def __str__(self):
        return f" Meeting holding at {self.name} on floor {self.floor_number} in room {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    # add foreign key room from Model Room to select a room when planning a meeting 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # CASCADE here means if room is deleted, all other meetings for that room would be deleted

    # add a representation method
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
