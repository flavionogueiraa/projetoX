# Generated by Django 3.2.12 on 2023-05-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_alter_estacaosolar_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacaosolar',
            name='nome',
        ),
    ]