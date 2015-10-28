from django.db import models

class Client(models.Model):
    identification = models.CharField(max_length=11, db_column='documento')
    name = models.CharField(max_length=80, db_column='nombres')
    details = models.TextField(db_column='detalles')

    def __str__(self):
        return 'name: %s, identification: %s' % (self.name, self.identification)
    def toJson(self):
        return {
                'documento' : self.identification, 
                'nombres': self.name, 
                'detalles': self.details
                }

    class Meta:
        db_table = 'clientes'