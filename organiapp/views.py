from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from website import models as website_models 

from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def checkout(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        adresse_ville = request.POST.get('adresse_ville')
        adresse_maison = request.POST.get('adresse_maison')
        town = request.POST.get('town')
        country_state = request.POST.get('country_state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        account_password = request.POST.get('account_password')
        order_notes = request.POST.get('order_notes')
        print(firstname, lastname, country, adresse_ville, adresse_maison, town, postcode, phone,  country_state, email, account_password, order_notes)
        try:
            validate_email(email)
            if email is not None and firstname is not None and lastname is not None and country is not None and adresse_ville is not None and adresse_maison is not None and town is not None and country_state is not None and postcode is not None and phone is not None and account_password is not None and order_notes is not None:
                check = models.Checkout(
                    firstname = firstname, 
                    lastname = lastname, 
                    country = country, 
                    adresse_ville = adresse_ville, 
                    adresse_maison = adresse_maison, 
                    country_state = country_state,
                    town = town, 
                    postcode = postcode,
                    phone = phone,
                    email = email,
                    account_password = account_password, 
                    order_notes = order_notes, 
                )
                check.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"Veuillez verifier les informations saisies")
                
        except Exception as e:
            print(e)
            messages.error(request, "L' enregistrement a échouer")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)

    datas = {
        'siteinfo':siteinfo,
        'reseau':reseau,


        "Checkout":"active"
    }
    return render(request, 'pages/checkout.html', datas)

def shop_details(request,slug):
    article = models.Article.objects.get(slug=slug)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)
    network = website_models.Reseau.objects.filter(status=True)
    details_shop = get_object_or_404(models.Article, slug=slug)
    orga = models.Article.objects.filter(status=True)
    datas = {

        'article':article,
        'siteinfo':siteinfo,
        'reseau':reseau,
        'network':network,
        'details_shop':details_shop,
        'orga':orga,

    }
    return render(request, 'pages/shop-details.html', datas)

def shop_grid(request):
    articles = models.Article.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)
    sale = models.Article.objects.filter(status=True)[:9]
    latest = models.Article.objects.filter(status=True).order_by('-date_update')[:6]

    
    article_list = models.Article.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(article_list, 4)
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)


    datas = {
        'articles':articles,
        'page':page,
        'siteinfo':siteinfo,
        'reseau':reseau,
        'sale':sale,
        'article':article,
        'latest':latest,
        'paginator':paginator,

    }
    return render(request, 'pages/shop-grid.html', datas)

def shoping_cart(request):
    articles = models.Article.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)

    datas = {
        'articles':articles,
        'siteinfo':siteinfo,
        'reseau':reseau,

    }
    return render(request, 'pages/shoping-cart.html', datas)
