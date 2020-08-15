from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt

# views.py handles http request
def welcome (request):
    return HttpResponse("Welcome to Meeting Planner")

def date (request):
    return HttpResponse("This page was served at "+str(dt.now()))

# add an About page that shows some text about yourself

def about (request):
    return HttpResponse("My name is Patrick and I am an django developer")
