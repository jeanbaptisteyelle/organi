# Generated by Django 2.2.12 on 2020-07-16 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_achat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_compte', models.CharField(max_length=255)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cart_achat',
                'verbose_name_plural': 'Cart_achats',
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('contry', models.CharField(max_length=250)),
                ('adresse_ville', models.CharField(max_length=250)),
                ('adresse_maison', models.CharField(max_length=250)),
                ('town', models.CharField(max_length=250)),
                ('postcode', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('account_password', models.CharField(max_length=180)),
                ('order_notes', models.CharField(max_length=250)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
            },
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Livraisaon',
                'verbose_name_plural': 'Livraisaons',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prix', models.CharField(max_length=50)),
                ('reduction', models.CharField(max_length=50)),
                ('prix_reduction', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('information', models.TextField()),
                ('poids', models.CharField(max_length=50)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livraison_article', to='organiapp.Livraison')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types_article', to='organiapp.Type')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilité', models.CharField(max_length=255)),
                ('jour_livraison', models.CharField(max_length=50)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiapp.Livraison')),
                ('share_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_reseau', to='website.Reseau')),
            ],
            options={
                'verbose_name': 'Achat',
                'verbose_name_plural': 'Achats',
            },
        ),
    ]
