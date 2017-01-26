from django.conf.urls import patterns, url
from perfis.views import index, exibir

#urlpatterns = patterns('',
 #   url(r'^$', 'perfis.views.index')
#)   
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfil$', exibir, name='exibir')
]