from django.db import models

class Office(models.Model):
    office = models.CharField(max_length=40, db_column='sede')
    address = models.CharField(max_length=40, db_column='direccion')

    class Meta:
        db_table = 'sedes'