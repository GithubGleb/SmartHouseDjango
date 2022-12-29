from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('ok')

def profile(request):
    return HttpResponseRedirect('https://ya.ru/')

def productinfo(request):
    return HttpResponse(content = b'Item list', status = 404)