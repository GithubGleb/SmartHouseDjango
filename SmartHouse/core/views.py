from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Userdatainput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import New_profile, Products, Controler
from django.core.paginator import Paginator
import datetime


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


def add_product(request):
    # products = Products(name='Жалюзи Пересвет', model='Л-2', condition='True')
    # products.save()
    # g = datetime.date.today()
    pro = New_profile(name='Генри',
                      surname='Актоев',
                      username='GanryAkto',
                      email='GenryAkto@include.com',
                      feedback='none',
                      grade='3',
                      author_id='1'
                      # date=g
                      )
    pro.save()
    # return render(request, 'add_product.html')
    return HttpResponse('Всё хорошо')


def get_all_profile(request):
    prof = New_profile.objects.all()
    # prod = Products.objects.all()
    # prof_list = [f'{p.name}, {p.surname}' for p in prof]
    # print(prof_list)
    context = {
        # 'prof': prof_list,
        # 'prod': prod,
        'prof': prof,
    }
    print(context)
    return render(request, 'all_list.html', context)

