# Generated by Django 3.2.12 on 2023-05-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0007_estacaosolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacaosolar',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicos.cliente', verbose_name='Cliente'),
        ),
    ]
