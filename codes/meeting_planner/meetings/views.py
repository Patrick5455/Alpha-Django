from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

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
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})


def show_room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/this_room.html", {"room": room})


#  create a class of modelform_factory
# it can generate a new class called ModelForm for us and ModelForm class can generate an html form

# it takes as argument, the model we want to base the form on.
# the exclude = [], means we want to see all the fields of the model
# so we are excluding an empty list

MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        # create an object of MeetingForm with user data (payload)
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
