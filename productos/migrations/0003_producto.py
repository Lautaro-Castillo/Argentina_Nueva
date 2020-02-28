# Generated by Django 3.0.3 on 2020-02-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20200226_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_fin', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(help_text='Descripcion del Producto', max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Marca')),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Rubro')),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Segmento')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'unique_together': {('rubro', 'segmento', 'marca', 'nombre')},
            },
        ),
    ]
