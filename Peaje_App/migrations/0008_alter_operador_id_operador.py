# Generated by Django 5.1 on 2024-10-16 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peaje_App', '0007_alter_operador_contraseña_alter_operador_id_operador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operador',
            name='id_operador',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]