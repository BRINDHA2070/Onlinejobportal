# Generated by Django 2.2.2 on 2020-06-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_auto_20200607_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_job',
            name='skills',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
