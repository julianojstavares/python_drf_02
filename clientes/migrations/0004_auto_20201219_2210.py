# Generated by Django 3.1.4 on 2020-12-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=25),
        ),
    ]
