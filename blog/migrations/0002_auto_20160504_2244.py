# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(to='blog.Category', blank=True, null=True),
        ),
    ]
