from django.shortcuts import render
from django.http import HttpResponse


# HTTP REQUEST #


def home(request):
    return HttpResponse('Home')
    # return HTTP Response #


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
