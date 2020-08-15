from django.shortcuts import render
from django.http import HttpResponse

# views.py handles http request
def welcome (request):
    return HttpResponse("Welcome to Meeting Planner")
