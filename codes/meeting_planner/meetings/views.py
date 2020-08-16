from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting
from meetings.models import Room


# Create your views here.

def detail(request, id):
    # get the meeting with a particular id

    # meeting = Meeting.objects.get(pk=id)

    # to handle error, we would not use the above Django get method,rather the below
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


# Add a new page that shows a list of all room objects

# Create a:
# -view
# - template
# - url mapping

def show_room(request):
    # rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all})


def show_room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/this_room.html", {"room": room})
