# Generated by Django 2.0.4 on 2018-04-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180427_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='ramo_atuacao',
            field=models.CharField(choices=[('Alimentos', 'Alimentos'), ('Automoveis', 'Automóveis'), ('Calçados', 'Calçados'), ('Esporte', 'Esporte'), ('Móveis', 'Móveis'), ('Roupa', 'Roupa'), ('Tecnologia', 'Tecnologia')], default='Alimentos', max_length=10),
        ),
    ]