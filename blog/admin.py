from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Categorie_infos', {'fields':['nom']}),
          ('standards', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Tag_infos', {'fields':['nom']}),
          ('standards', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Recette_infos', {'fields':['nom','description','image','methode','categorie','tag']}),
          ('standard', {'fields':['status']}),
          ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'




