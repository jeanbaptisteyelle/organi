# Generated by Django 2.2.12 on 2020-07-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiapp', '0008_auto_20200717_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='produit',
            field=models.ImageField(null=True, upload_to='image/promotion'),
        ),
    ]
