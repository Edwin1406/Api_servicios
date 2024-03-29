# Generated by Django 5.0.2 on 2024-02-08 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicio_riego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=100)),
                ('detalle_servicio', models.TextField(max_length=400)),
                ('valor_servicio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_cotizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicios', to='api.tipo_cotizacion')),
            ],
        ),
    ]
