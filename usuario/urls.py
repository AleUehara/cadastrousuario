'''
from django.conf.urls.defaults import *

from banco import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
'''

from django.conf.urls.defaults import *

from usuario import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)