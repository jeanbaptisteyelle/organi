# Generated by Django 2.2.12 on 2020-07-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Newletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Newletter',
                'verbose_name_plural': 'Newletters',
            },
        ),
        migrations.CreateModel(
            name='Reseau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('lien', models.URLField()),
                ('icones', models.CharField(choices=[('fa fa-facebook', 'facebook'), ('fa fa-instagram', 'instagram'), ('fa fa-twitter', 'twitter'), ('fa fa-pinterest', 'pinterest')], max_length=255)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Reseau',
                'verbose_name_plural': 'Reseaus',
            },
        ),
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/siteinfo')),
                ('email', models.EmailField(max_length=254)),
                ('livraison', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=50)),
                ('copyrights', models.CharField(max_length=255)),
                ('name_du_apdater', models.CharField(max_length=255)),
                ('commentaire', models.CharField(max_length=255)),
                ('open_time', models.TimeField()),
                ('url_marp', models.TextField()),
                ('icone', models.CharField(choices=[('fa fa-shopping-bag', 'shoping'), ('fa fa-heart', 'heart')], max_length=255)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Siteinfo',
                'verbose_name_plural': 'Siteinfos',
            },
        ),
    ]
