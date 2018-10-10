# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='peso',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
