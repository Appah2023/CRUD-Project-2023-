# Generated by Django 4.2 on 2023-05-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPCODE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
