# Generated by Django 5.1.4 on 2025-01-21 02:01

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pages/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Sin nombre', max_length=100)),
                ('apellido', models.CharField(default='Sin apellido', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('biografia', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinos.bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('calificacion', models.IntegerField()),
                ('vino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinos.vino')),
            ],
        ),
    ]
