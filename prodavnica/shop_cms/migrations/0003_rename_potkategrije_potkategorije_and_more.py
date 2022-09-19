# Generated by Django 4.0.3 on 2022-03-19 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cms', '0002_potkategrije'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Potkategrije',
            new_name='Potkategorije',
        ),
        migrations.AlterModelOptions(
            name='kategorije',
            options={'verbose_name_plural': 'Kategorije'},
        ),
        migrations.AlterModelOptions(
            name='potkategorije',
            options={'verbose_name_plural': 'Potkategorije'},
        ),
        migrations.RenameField(
            model_name='potkategorije',
            old_name='naziv_potkategrije',
            new_name='naziv_potkategorije',
        ),
    ]
