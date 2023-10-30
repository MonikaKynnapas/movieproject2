# Generated by Django 4.2.6 on 2023-10-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common', models.CharField(max_length=100)),
                ('official', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('subregion', models.CharField(blank=True, max_length=100, null=True)),
                ('flag', models.CharField(max_length=100)),
                ('map', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'ordering': ['common'],
            },
        ),
    ]
