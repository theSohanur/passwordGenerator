from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'pass': "djfadhf9hfwe23"})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-;:\/.<>'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 12))
    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thePassword})


def about(request):
    return render(request, 'generator/about.html')