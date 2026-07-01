from django.shortcuts import render
from django.http import HttpResponse


# HTTP REQUEST #


def home(request):
    return render(request, 'recipes/pages/home.html')
    # return HTTP Response #
