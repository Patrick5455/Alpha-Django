from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting

# Create your views here.

def detail(request, id):
    # get the meeting with a particular id
    
    #meeting = Meeting.objects.get(pk=id)

    # to handle error, we would not use the above Django get method,rather the below
    meeting = get_object_or_404(Meeting, pk=id)
    return render (request, "detail.html", {"meeting":meeting})


