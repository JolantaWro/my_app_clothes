# Generated by Django 4.1.4 on 2023-01-20 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='donation',
            options={'verbose_name': 'Donation', 'verbose_name_plural': 'Darowizny'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'verbose_name': 'Institution', 'verbose_name_plural': 'Instytucje'},
        ),
    ]
