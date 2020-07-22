from django.db import models
from website.models import Reseau

from django.utils.text import slugify 
import time
zips = time.time()
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.nom


class Recette(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/recettes')
    methode = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="recette_categorie", null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null= True, blank=True)

    def save(self, *args, **kwargs):
        self.slug ='-'.join((slugify(self.nom), (slugify(zips))))
        super(Recette, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Recette")
        verbose_name_plural = ("Recettes")

    def __str__(self):
        return self.nom