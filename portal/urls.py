from django.urls import re_path, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('protected', views.ProtectedView.as_view(), name='protected_view'),
    path('unprotected', views.UnprotectedView.as_view(), name='unprotected_view'),
    re_path(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
]
