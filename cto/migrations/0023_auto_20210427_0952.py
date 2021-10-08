# Generated by Django 3.0.7 on 2021-04-27 14:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0022_auto_20210426_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='partes',
            name='estatusParte',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estatus '),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='caracteristicasPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Características'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='conocimientosPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Conocimientos'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='experienciaPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Experiencia'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='funcionesPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Funciones'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='habilidadesPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Habilidades'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='herramientasPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Herramientas'),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nombrePuesto',
            field=models.CharField(max_length=100, verbose_name='Nombre del puesto'),
        ),
    ]