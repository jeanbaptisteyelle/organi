from django.db import models
from website.models import Reseau
from user.models import UserProfile
from django.utils.text import slugify 
import time
zips = time.time()
# Create your models here.


class Type(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Type")
        verbose_name_plural = ("Types")

    def __str__(self):
        return self.nom


class Livraison(models.Model):
    message = models.CharField(max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Livraisaon")
        verbose_name_plural = ("Livraisaons")

    def __str__(self):
        return self.message


class Article(models.Model):
    types = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='types_article')
    nom = models.CharField(max_length=255)
    pub = models.CharField(max_length=255, null=True)
    prix = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/article', null=True)
    reduction = models.CharField(max_length=50)
    prix_reduction = models.CharField(max_length=50)
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE, related_name='livraison_article')
    description = models.TextField()
    information = models.TextField()
    poids = models.CharField(max_length=50)

    slug = models.SlugField(unique=True, null= True, blank=True)

    def save(self, *args, **kwargs):
        self.slug ='-'.join((slugify(self.nom), (slugify(zips))))
        super(Article, self).save(*args, **kwargs)
    

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.nom


class Promotion(models.Model):
    produit = models.ImageField(upload_to='image/promotion', null=True)
    composition = models.CharField(max_length=250)
    titre = models.CharField(max_length=250)
    date_add = models.DateField(auto_now_add=True, null=True)
    date_update = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, null=True)
    class Meta:
        verbose_name = ("Promotion")
        verbose_name_plural = ("Promotions")

    def __str__(self):
        return self.titre


class Achat(models.Model):
    disponibilité = models.CharField(max_length=255)
    share_on = models.ForeignKey(Reseau, on_delete=models.CASCADE, related_name='share_reseau')
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    jour_livraison = models.CharField(max_length=50)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Achat")
        verbose_name_plural = ("Achats")
    def __str__(self):
        return self.disponibilité


class Checkout(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    adresse_ville = models.CharField(max_length=250) 
    adresse_maison = models.CharField(max_length=250)  
    town = models.CharField( max_length=250)
    country_state = models.CharField( max_length=250, null=True)
    postcode = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    account_password = models.CharField(max_length=180)
    order_notes = models.CharField(max_length=250)


    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Checkout")
        verbose_name_plural = ("Checkouts")

    def __str__(self):
        return self.firstname

class Cart_achat(models.Model):
    code_compte = models.CharField(max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Cart_achat")
        verbose_name_plural = ("Cart_achats")

    def __str__(self):
        return self.code_compte

class Panier(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.CharField(max_length=250)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Panier")
        verbose_name_plural = ("Paniers")

    def __str__(self):
        return self.quantite
