# Generated by Django 5.1 on 2024-10-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peaje_App', '0005_alter_operador_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operador',
            name='id_operador',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]