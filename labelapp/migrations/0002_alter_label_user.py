# Generated by Django 3.2.13 on 2022-04-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
