# Generated by Django 3.0.6 on 2020-05-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_todowoorks_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todowoorks',
            name='fileupload',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]