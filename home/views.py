from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.db import connection
import random
from django.contrib.auth.hashers import make_password
import math
import requests

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def darkmod(request):
    return render(request, 'dark.html')