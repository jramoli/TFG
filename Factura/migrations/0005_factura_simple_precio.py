# Generated by Django 4.0.1 on 2022-01-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factura', '0004_factura_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura_simple',
            name='precio',
            field=models.FloatField(default=0.0),
        ),
    ]
