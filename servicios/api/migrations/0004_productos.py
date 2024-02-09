# Generated by Django 5.0.2 on 2024-02-08 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_servicio_riego_id_cotizacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_producto', models.IntegerField()),
                ('id_cotizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos', to='api.tipo_cotizacion')),
            ],
        ),
    ]