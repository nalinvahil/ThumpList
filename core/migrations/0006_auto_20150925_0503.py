# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150925_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.TextField(null=True, blank=True),
        ),
    ]
