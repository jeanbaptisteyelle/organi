# Generated by Django 2.2.12 on 2020-07-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='open_time',
            field=models.CharField(max_length=100),
        ),
    ]
