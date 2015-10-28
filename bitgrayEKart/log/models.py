from django.db import models

class Log(models.Model):
    createdAt = models.DateTimeField(auto_add_now=True, db_column='fecha')
    details = models.TextField(db_column='descripcion')

    class Meta:
        db_table = 'log'