# Generated by Django 3.1.2 on 2020-11-02 21:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('get_handling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='long_and_short',
            name='newfield',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
