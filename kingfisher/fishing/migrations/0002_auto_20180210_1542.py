# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='fishing_license',
            field=models.ImageField(blank=True, null=True, upload_to='licenses/', verbose_name='Av lisans\u0131'),
        ),
    ]