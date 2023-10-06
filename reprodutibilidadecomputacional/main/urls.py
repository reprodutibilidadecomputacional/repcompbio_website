from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls import url, include

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('instafeed/', views.instafeed, name='instafeed'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('contato/', views.contact, name='contato'),
    #path('ebook/', views.ebook, name='ebook'),
    url(r'^docs/', include('django_mkdocs.urls', namespace='documentation')),
    path('apoio/', views.apoio, name='apoio'),
    path('participe/', views.participe, name='participe'),

]

urlpatterns += staticfiles_urlpatterns()
