# Generated by Django 3.2.12 on 2023-05-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf_cnpj',
            field=models.CharField(max_length=30, verbose_name='CPF'),
        ),
    ]