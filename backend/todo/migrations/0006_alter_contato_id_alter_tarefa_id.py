# Generated by Django 4.1.1 on 2022-09-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_contato_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]