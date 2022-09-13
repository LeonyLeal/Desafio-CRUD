# Generated by Django 4.1.1 on 2022-09-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=255)),
                ('data_alteracao', models.DateTimeField()),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tarefa',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('contato_id', models.IntegerField()),
                ('titulo', models.CharField(max_length=120)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('data_alteracao', models.DateTimeField()),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]