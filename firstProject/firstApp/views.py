from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>My first Django App</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b>Current Date and time: </b>"+str(dt)
    return HttpResponse(s)