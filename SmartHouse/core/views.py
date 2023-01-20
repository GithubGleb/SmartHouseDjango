from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Userdatainput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import New_profile
from django.core.paginator import Paginator


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
    name = request.GET.get("name", 'Клиент')
    context = {
        'name': name,
    }
    return render(request, 'index.html', context)


CONTENT = [str(i) for i in range(1000)]


def paginationproduct(request):
    num_page = request.GET.get('page', 1)
    paginator = Paginator(CONTENT, 11)
    page = paginator.get_page(int(num_page))
    context = {
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'product.html', context)


def product_info(request):
    return HttpResponse(content=b'Item list', status=404)
