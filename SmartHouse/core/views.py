from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Userdatainput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import New_profile


#

class new_profileView(LoginRequiredMixin, CreateView):
    model = New_profile
    fields = ['name', 'surname', 'username', 'email', 'feedback', 'grade']
    success_url = 'add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get(self, request):
    #     form = Userdatainput()
    #     return render(request, 'new_profile.html', {'form': form})
    #
    # def post(self, request):
    #     form = Userdatainput(request.POST)
    #     if form.is_valid():
    #         context = form.cleaned_data
    #         return render(request, 'new_profile.html', context)
    #     else:
    #         return render(request, '404.html', {'error': form.errors})

class New_profileListView(LoginRequiredMixin, ListView):
    model = New_profile

    def get_queryset(self):
        if self.request.user.is_staff:
            return New_profile.objects.all()
        return New_profile.objects.filter(author=self.request.user)

def index(request):
    return HttpResponse('ok')


def new_profile(request):
    return HttpResponseRedirect('https://ya.ru/')


def product_info(request):
    return HttpResponse(content=b'Item list', status=404)
