from django.db import models

from clients.models import Client
from products.models import Product
from offices.models import Office

class Order(models.Model):
    client = models.ForeignKey(Client, db_column='id_cliente')
    product = models.ForeignKey(Product, db_column='id_producto')
    office = models.ForeignKey(Office, db_column='id_sede', null=True)
    price = models.IntegerField(db_column='precio')
    description = models.TextField(db_column='descripcion')
    createdAt = models.DateTimeField(auto_now_add=True, db_column='fecha')

    def __unicode__(self):
        return 'client: %s, product: %s, office: %s, price: %s' % (client.name, product.product, office.office, price)

    def toJson(self):
        return {
            'Cliente': {'id': self.client.pk, 'nombre': self.client.name},
            'Producto': {'id': self.product.pk, 'producto': self.product.product},
            'Oficina': {'id': self.office.pk, 'sede': self.office.office},
            'Precio': self.price,
            'Descripcion': self.description
        }
        
    class Meta:
        db_table = 'compras'