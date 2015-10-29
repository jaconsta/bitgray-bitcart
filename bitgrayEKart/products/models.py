from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=40, db_column='producto')
    price = models.IntegerField(db_column='precio')
    details = models.TextField(db_column='descripcion')

    def __unicode__(self):
        return 'Product: %s, price: %s.' % (self.product, self.price)
    def toJson(self):
        return {
                'producto': self.product,
                'precio': self.price,
                'descripcion': self.details
               }

    class Meta:
        db_table = 'productos'
