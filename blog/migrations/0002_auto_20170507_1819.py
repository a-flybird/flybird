# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateField(),
        ),
    ]
