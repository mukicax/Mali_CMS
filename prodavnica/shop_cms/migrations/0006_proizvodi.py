# Generated by Django 4.0.3 on 2022-03-22 17:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cms', '0005_rename_address_kupci_adresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proizvodi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('naziv_proizvoda', models.CharField(max_length=200)),
                ('opis_proizvoda', models.TextField(max_length=1000)),
                ('kupac_veza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_cms.kupci')),
                ('potkategorija_veza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_cms.potkategorije')),
            ],
            options={
                'verbose_name_plural': 'Proizvodi',
            },
        ),
    ]
