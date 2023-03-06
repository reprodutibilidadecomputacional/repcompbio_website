from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('instafeed/', views.instafeed, name='instafeed'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('contact/', views.contact, name='contact'),
    path('ebook/', views.ebook, name='ebook'),
    path('apoio/', views.apoio, name='apoio'),
    path('participe/', views.participe, name='participe'),
]

urlpatterns += staticfiles_urlpatterns()
