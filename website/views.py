from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting 


def welcome(request):
    return render(request, "website/welcome.html",
    {"message":"This was a message you were looking for", "x":"25", "num_meetings":Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was served at "+ str(datetime.now()))

def about(request):
    return HttpResponse("I am adding an About page")
