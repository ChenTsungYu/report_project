# Generated by Django 3.0.6 on 2020-05-20 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('products', '0001_initial'),
        ('reports', '0005_auto_20200520_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='report',
            name='production_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.ProductionLine'),
        ),
    ]
