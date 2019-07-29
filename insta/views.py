from django.shortcuts import render
import datetime as dt
from django.http import Http404

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Insta')

