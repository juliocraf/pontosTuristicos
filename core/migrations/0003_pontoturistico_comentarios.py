# Generated by Django 5.0.3 on 2024-03-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0002_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.comentario'),
        ),
    ]
