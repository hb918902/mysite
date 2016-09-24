# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160529_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.SmallIntegerField(default=0, choices=[(0, '草稿'), (1, '发布'), (2, '删除')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='cre_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
