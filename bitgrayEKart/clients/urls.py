from django.conf.urls import url

from . import views 

urlpatterns = [
    # /clients/
    url(r'^$', views.index, name='clientsCr'),
    url(r'^(?P<clientId>[0-9]+)$', views.crud, name='clientsUD')
]