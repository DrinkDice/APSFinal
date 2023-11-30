# Generated by Django 4.2.7 on 2023-11-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_filme', models.CharField(default='', max_length=255)),
                ('data_lancamento', models.DateField(default='')),
                ('nome_diretor', models.CharField(default='', max_length=255)),
                ('nota', models.DecimalField(decimal_places=1, default='0', max_digits=3)),
            ],
        ),
    ]