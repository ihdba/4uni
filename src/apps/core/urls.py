from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects', include('apps.projects.urls'), name='projects'),
    path('partners', include('apps.partners.urls'), name='partners'),
    path('eshop', include('apps.eshop.urls'), name='eshop'),
]