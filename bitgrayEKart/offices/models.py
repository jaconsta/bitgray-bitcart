from django.db import models

class Office(models.Model):
    office = models.CharField(max_length=40, db_column='sede')
    address = models.CharField(max_length=40, db_column='direccion')

    def __unicode__(self):
        return 'Office: %s, address: %s' % (office, address)
    def toJson(self):
        return {
                    'oficina': self.office,
                    'direccion': self.address
               }

    class Meta:
        db_table = 'oficinas'
