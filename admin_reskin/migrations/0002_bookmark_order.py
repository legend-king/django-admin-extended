# Generated by Django 3.2 on 2021-10-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_reskin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]