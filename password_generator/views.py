import string, random

from django.shortcuts import render
from django.http import HttpResponse


# Create views here


def home(request):
    numbers = list(str(x) for x in range(8, 17))
    return render(request, 'generator/home.html', {'dim': numbers})


def password(request):
    characters = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    numbers = list(str(x) for x in range(10))
    special = list(string.punctuation)

    if request.GET.get('uppercase'):
        characters.extend(upper)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    length = int(request.GET.get('length', default=8))

    chars = characters
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    characters = list(string.ascii_lowercase)

    return render(request, 'generator/password.html', {'password': thepassword, 'string': ''.join(chars)})


def aboutme(request):
    return render(request, 'generator/aboutme.html')
