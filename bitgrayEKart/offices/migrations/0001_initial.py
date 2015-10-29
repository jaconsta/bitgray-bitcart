# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('office', models.CharField(max_length=40, db_column='sede')),
                ('address', models.CharField(max_length=40, db_column='direccion')),
            ],
            options={
                'db_table': 'oficinas',
            },
        ),
    ]
