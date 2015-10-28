from django.db import models

from clients.models import Client
from products.models import  Product
from offices.models import Office

class Purchase(models.Model):
    client = models.ForeignKey(Client, db_column='id_cliente')
    product = models.ForeignKey(Product, db_column='id_producto')
    office = models.ForeignKey(Office, db_column='id_sede')
    price = models.IntegerField(db_column='precio')
    description = models.TextField(db_column='descripcion')
    createdAt = models.DateTimeField(auto_add_now=True, db_column='fecha')

    class Meta:
        db_table = 'compras'