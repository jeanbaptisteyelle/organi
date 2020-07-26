from django.db import models
from django import forms
# Create your models here.

class Search(forms.Form):
    searching = forms.CharField( max_length=100)

class Siteinfo(models.Model):
    logo = models.ImageField( upload_to='logo/siteinfo')
    email = models.EmailField()
    livraison = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=50)
    copyrights = models.CharField(max_length=255)
    name_du_apdater = models.CharField(max_length=255)
    commentaire = models.CharField(max_length=255)
    open_time = models.CharField(max_length=100)
    url_marp = models.TextField()
    partenaire = models.ImageField(upload_to='image/partenaires', null='True')


    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Siteinfo")
        verbose_name_plural = ("Siteinfos")

    def __str__(self):
        return self.telephone


class Reseau(models.Model):
    ICONES = [
        ('fa fa-facebook', 'facebook'),
        ('fa fa-instagram', 'instagram'),
        ('fa fa-twitter', 'twitter'),
        ('fa fa-pinterest', 'pinterest'),
        ('fa fa-linkedin', 'linkedin'),
        ('fa fa-google-plus', 'google-plus'),
        ('fa fa-envelope', 'envelope'),
       

    ]
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icones = models.CharField(choices = ICONES ,max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Reseau")
        verbose_name_plural =("Reseaux")

    def __str__(self):
        return self.nom
    
class Newletter(models.Model):
    email = models.EmailField(max_length=254)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Newletter")
        verbose_name_plural = ("Newletters")

    def __str__(self):
        return str(self.email)


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    message = models.TextField()


    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.nom
