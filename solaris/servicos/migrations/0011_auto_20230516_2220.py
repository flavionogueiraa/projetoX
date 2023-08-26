# Generated by Django 3.2.12 on 2023-05-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0010_visita_realizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacaosolar',
            name='kw_placa',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='kW/h da placa'),
        ),
        migrations.AddField(
            model_name='estacaosolar',
            name='valor_cada_placa',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Valor de cada placa'),
        ),
        migrations.AlterField(
            model_name='estacaosolar',
            name='geracao_mensal',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Geração mensal por placa (kWh)'),
        ),
    ]