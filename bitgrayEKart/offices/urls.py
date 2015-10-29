from django.conf.urls import url

from . import views

urlpatterns = [
    # /offices/
    url(r'^$', views.index, name='officesCr'),
    url(r'^(?P<officeId>[0-9]+)$', views.crud, name='officesUD')
]
