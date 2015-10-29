from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='productsCr'),
    url(r'^(?P<productId>[0-9]+)$', views.crud, name='productsUD')
]
