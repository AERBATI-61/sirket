# Generated by Django 3.2.4 on 2021-12-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Migros', '0009_auto_20211224_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urunler',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='misyon',
            field=models.TextField(default='sdc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='visyon',
            field=models.TextField(default='sad'),
            preserve_default=False,
        ),
    ]
