# Generated by Django 2.2.10 on 2021-09-17 05:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210917_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, size=None),
        ),
    ]