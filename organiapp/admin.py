from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('Type_infos', {'fields':['nom']}),
    ('standard', {'fields':['status']}),
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


@admin.register(models.Livraison)
class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('message','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('message',)
    date_hierarchy = 'date_add'
    list_display_links = ['message']
    fieldsets = [
    ('Livraison_infos', {'fields':['message']}),
    ('standard', {'fields':['status']}),
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


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','reduction','prix_reduction','poids','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('Livraison_infos', {'fields':['types','nom','prix','reduction','prix_reduction','livraison','pub','description','information','poids','image']}),
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

@admin.register(models.Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ('disponibilité','share_on','livraison','jour_livraison','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['disponibilité']
    fieldsets = [
    ('Achat_infos', {'fields':['disponibilité','share_on','livraison','jour_livraison']}),
    ('standard', {'fields':['status']}),
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

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('titre','composition','date_add','date_update','status','produit_view')
    list_filter = ('date_add','date_update','status', 'produit')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('Achat_infos', {'fields':['titre','composition','produit']}),
    ('standard', {'fields':['status']}),
    ]

    def produit_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.produit.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'






@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','country','postcode','email','account_password','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
    ('Checkout_infos', {'fields':['firstname','lastname','country','adresse_ville','adresse_maison','town','postcode','phone','email','account_password','order_notes']}),
    ('standard', {'fields':['status']}),
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


@admin.register(models.Cart_achat)
class Cart_achatAdmin(admin.ModelAdmin):
    list_display = ('code_compte','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('code_compte',)
    date_hierarchy = 'date_add'
    list_display_links = ['code_compte']
    fieldsets = [
    ('Checkout_infos', {'fields':['code_compte']}),
    ('standard', {'fields':['status']}),
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
