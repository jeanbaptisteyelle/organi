from django.shortcuts import render, redirect
from . import models
from organiapp import models as organiapp_models
from blog import models as blog_models

from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def newletter(request):
    if request.method=='POST':
        email = request.POST.get('email')
        print(email)
        try:
            validate_email(email)
            if  email is not None:
                letter = models.Newletter(
                    email = email,
                )
                letter.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
                
        except Exception as e:
            print(e)
            messages.error(request, "l'enregistrement à echoué")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
    article = organiapp_models.Article.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = models.Reseau.objects.filter(status=True)
    featured = organiapp_models.Article.objects.filter(status=True)[:8]
    promotion = organiapp_models.Promotion.objects.filter(status=True)[:3]
    latest =  organiapp_models.Article.objects.filter(status=True).order_by('-date_update')[:6]
    recette = blog_models.Recette.objects.filter(status=True)[:3]

    datas = {
        'siteinfo':siteinfo,
        'reseau':reseau,
        "article":article,
        "featured":featured,
        "promotion":promotion,
        "latest":latest,
        "recette":recette,


       
    }
    return render(request, 'pages/index.html', datas)

def contact(request):
    if request.method=='POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(nom, email, message)
        try:
            validate_email(email)
            if  email is not None and not nom.isspace() and nom is not None and message is not None :
                contact = models.Contact(
                    email = email,
                    nom = nom,
                    message = message,

                )
                contact.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
                
        except:
            messages.error(request, "veuillez entrer un email correct")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

    reseau = models.Reseau.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    datas = {
        'siteinfo':siteinfo,
        'reseau':reseau,
    }
    return render(request, 'pages/contact.html', datas)