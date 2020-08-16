from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
from meetings.models import Meeting
 

# views.py handles http request
def welcome (request):
    #return HttpResponse("Welcome to Meeting Planner")

# to add a template page, we return a render page:
# it will take as first argument, request and second argument, 
# the name of the page and it's relativepath

    return render(request, "website/welcome.html", {"message":
    "This is a message to test django templating",
     "num_meetings": Meeting.objects.count()}) 

def date (request):
    return HttpResponse("This page was served at "+str(dt.now()))

# add an About page that shows some text about yourself

def about (request):
    return HttpResponse("My name is Patrick and I am an django developer")