from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_profileView.as_view()),
    # path('', views.new_profileView.as_view()),
]