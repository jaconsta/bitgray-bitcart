from django.conf.urls import url

from . import views 

urlpatterns = [
    # /orders/
    url(r'^$', views.index, name='ordersCr'),
    url(r'^(?P<orderId>[0-9]+)$', views.crud, name='ordersUD')
]