# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
