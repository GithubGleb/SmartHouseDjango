from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
#


class new_profileView(View):
    def get(self, request):
        return render(request, 'new_profile.html', {})


def index(request):
    return HttpResponse('ok')


def new_profile(request):
    return HttpResponseRedirect('https://ya.ru/')


def product_info(request):
    return HttpResponse(content=b'Item list', status=404)
