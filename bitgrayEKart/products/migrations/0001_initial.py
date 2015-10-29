# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=40, db_column='producto')),
                ('price', models.IntegerField(db_column='precio')),
                ('details', models.TextField(db_column='descripcion')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]
