# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('offices', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.IntegerField(db_column='precio')),
                ('description', models.TextField(db_column='descripcion')),
                ('createdAt', models.DateTimeField(db_column='fecha', auto_now_add=True)),
                ('client', models.ForeignKey(db_column='id_cliente', to='clients.Client')),
                ('office', models.ForeignKey(db_column='id_sede', to='offices.Office')),
                ('product', models.ForeignKey(db_column='id_producto', to='products.Product')),
            ],
            options={
                'db_table': 'compras',
            },
        ),
    ]
