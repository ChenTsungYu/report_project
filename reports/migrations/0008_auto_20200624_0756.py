# Generated by Django 3.0.6 on 2020-06-24 07:56

from django.db import migrations, models
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20200520_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreported',
            name='problem_id',
            field=models.CharField(blank=True, default=reports.models.random_code, max_length=12, unique=True),
        ),
    ]
