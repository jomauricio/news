# Generated by Django 4.1.5 on 2023-03-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='cpf',
            field=models.CharField(blank=True, max_length=15, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
    ]
