from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=40, db_column='producto')
    price = models.IntegerField(db_column='precio')
    details = models.TextField(db_column='descripcion')

    class Meta:
        db_table = 'productos'