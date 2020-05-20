# Generated by Django 3.0.6 on 2020-05-20 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('reports', '0003_auto_20200520_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemReported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('problem_id', models.CharField(blank=True, max_length=12, unique=True)),
                ('breakdown', models.PositiveIntegerField()),
                ('public', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
