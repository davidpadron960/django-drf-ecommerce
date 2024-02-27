# Generated by Django 5.0.2 on 2024-02-27 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_alter_producto_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='producto.categoria'),
        ),
    ]
