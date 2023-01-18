from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Userdatainput
from django.contrib.auth.mixins import LoginRequiredMixin
#

class new_profileView(LoginRequiredMixin, View):
    def get(self, request):
        form = Userdatainput()
        return render(request, 'new_profile.html', {'form': form})

    def post(self, request):
        form = Userdatainput(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'new_profile.html', context)
        else:
            return render(request, '404.html', {'error': form.errors})

def index(request):
    return HttpResponse('ok')


def new_profile(request):
    return HttpResponseRedirect('https://ya.ru/')


def product_info(request):
    return HttpResponse(content=b'Item list', status=404)
