from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('contato/', views.contact, name='contato'),
    path('ebook/', views.ebook, name='ebook'),
    path('apoio/', views.apoio, name='apoio'),
    path('participe/', views.participe, name='participe')
]

urlpatterns += staticfiles_urlpatterns()
