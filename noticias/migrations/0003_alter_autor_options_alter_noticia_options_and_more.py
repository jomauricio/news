# Generated by Django 4.1.5 on 2023-03-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name_plural': 'Noticias'},
        ),
        migrations.AddField(
            model_name='noticia',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='imagens', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='cpf',
            field=models.CharField(max_length=15, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to='noticias.autor', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='conteudo',
            field=models.TextField(verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_pub',
            field=models.DateField(verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
