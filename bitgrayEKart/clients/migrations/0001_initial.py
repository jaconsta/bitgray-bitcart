# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('identification', models.CharField(db_column='documento', max_length=11)),
                ('name', models.CharField(db_column='nombres', max_length=80)),
                ('details', models.TextField(db_column='detalles')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
    ]
