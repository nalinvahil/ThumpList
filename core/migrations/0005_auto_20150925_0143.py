# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Alternative'), (2, b'Country'), (3, b'Electronic'), (4, b'Dance'), (5, b'Hip-Hop/Rap'), (6, b'Jazz'), (7, b'Pop'), (8, b'R&B/Soul'), (9, b'Rock'), (10, b'Reggae')]),
        ),
    ]
