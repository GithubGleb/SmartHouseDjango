from django.urls import path, include
from . import views


urlpatterns = [
    path('add', views.new_profileView.as_view(), name='new_profile-create'),
    path('', views.New_profileListView.as_view(), name='new_profile-list'),
    path('', include('smarthouseblog.urls')),
    path('', include('APISmartHouse.urls')),
]