# Generated by Django 4.0.5 on 2022-08-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(db_column='Numero', unique=True)),
                ('cvv', models.IntegerField(db_column='CVV')),
                ('fecha_de_otorgamiento', models.DateField(db_column='Fecha de otorgamiento')),
                ('fecha_de_expiracion', models.DateField(db_column='Fecha de expiracion')),
                ('credito_debito', models.IntegerField(db_column='Credito/debito')),
                ('marca_tarjeta', models.IntegerField(db_column='Marca tarjeta')),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
    ]
