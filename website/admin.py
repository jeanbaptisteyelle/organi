from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('name_du_apdater','adresse','telephone','copyrights','date_add','date_update','status','logo_view','partenaire_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('name_du_apdater',)
    date_hierarchy = 'date_add'
    list_display_links = ['name_du_apdater']
    fieldsets = [
          ('Site_infos', {'fields':['email','livraison','adresse','telephone','copyrights','name_du_apdater','commentaire','open_time','url_marp','logo','partenaire']}),
          ('standard', {'fields':['status']}),
          ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))
    
    def partenaire_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.partenaire.url))

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Reseau)
class ReseauAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Reseau_infos', {'fields':['nom','lien','icones']}),
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


@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
          ('Newletter_infos', {'fields':['email']}),
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


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','email','message','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Contact_infos', {'fields':['nom','email','message']}),
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