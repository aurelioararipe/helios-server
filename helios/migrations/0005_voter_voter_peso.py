# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0004_auto_20170528_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='voter_peso',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
