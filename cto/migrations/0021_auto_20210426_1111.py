# Generated by Django 3.0.7 on 2021-04-26 16:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0020_auto_20210209_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puestos',
            name='actividadesPuesto',
        ),
        migrations.AddField(
            model_name='puestos',
            name='caracteristicasPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Características del puesto'),
        ),
        migrations.AddField(
            model_name='puestos',
            name='cpnocimientosPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Conocimientos del puesto'),
        ),
        migrations.AddField(
            model_name='puestos',
            name='experienciaPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Experiencia del puesto'),
        ),
        migrations.AddField(
            model_name='puestos',
            name='funcionesPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Funciones del puesto'),
        ),
        migrations.AddField(
            model_name='puestos',
            name='habilidadesPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Habilidades del puesto'),
        ),
        migrations.AddField(
            model_name='puestos',
            name='herramientasPuesto',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Herramientas del puesto'),
        ),
    ]