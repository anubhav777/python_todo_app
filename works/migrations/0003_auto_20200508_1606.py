# Generated by Django 3.0.6 on 2020-05-08 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0002_auto_20200507_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todowoorks',
            name='userid',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]