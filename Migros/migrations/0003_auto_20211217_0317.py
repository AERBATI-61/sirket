# Generated by Django 3.2.4 on 2021-12-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Migros', '0002_auto_20211217_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
        migrations.AlterField(
            model_name='urunler',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
