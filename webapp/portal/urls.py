from django.urls import re_path, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    re_path(r'^$', TemplateView.as_view(template_name='homepage.html')),
]
