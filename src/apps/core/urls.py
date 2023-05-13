from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects', include('apps.projects.urls'), name='projects'),
    path('eshop', include('apps.eshop.urls'), name='eshop'),
    path('suppliers', include('apps.suppliers.urls'), name='suppliers'),
    path('features', include('apps.design.urls'), name='features'),
]