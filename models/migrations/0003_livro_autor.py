# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(default=1, to='models.Autor'),
            preserve_default=False,
        ),
    ]
