from django.shortcuts import render,redirect
from . import models
from organiapp import models as organiapp_models
from blog import models as blog_models

from django.db.models import Q

from django.contrib.auth import authenticate,login,logout
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def login_log(request):
    success = False
    message=""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            print("login échoué")
            success = True
            message = "Connexion echoué, merci de vérifier vos informations"
    datas = {
        "success":success,
        "message":message,
    }
    return render(request, 'pages/login.html', datas)


def register(request):
    success = False
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        print(username,email,password,confirm)
        if password != confirm:
            success = True
            message = "mot de passe incorrect"
            print("mot de passe incorrect")
        else:
            message = "correct"
            print("success")
            try:
                print("1")
                validate_email(email)
                isemail = True
                if isemail and not email.isspace() and username is not None and password is not None and confirm is not None:
                    try:
                        print("2")
                        try:
                            exist_user = User.objects.get(username=username)
                        except :
                            exist_user = User.objects.get(email=email)

                        message = "un utilisateur avec le même username ou email est déjà connecté"
                        success = True 
                    except Exception as e :
                        print("3", e)
                        user = User(
                            username=username,
                            email=email,
                            password=password,
                        )
                        user.save() 
                        user.password = password
                        user.set_password(user.password)
                        user.save()

                        try:
                            us = authenticate(username=username, password=password)
                            if us.is_active:
                                login(request,us)
                                return redirect('login')
                        except Exception as e:
                            print("4", e)


            except Exception as e:
                success = True 
                print("5", e)
                message = "l'inscription a échoué, veuillez remplir le formulaire correctement"
                print("inscription echoué")
    datas = {
        "success":success,
        "message":message,
        }

    return render(request, 'pages/register.html', datas)

def deconnexion(request):
    logout(request)
    return redirect('login')

def search(request):
    if request.method=='POST' and len(request.POST.get('searching').strip()) > 0:

        result = request.POST.get('searching')
        siteinfo = models.Siteinfo.objects.filter(status=True).latest('-date_update')
        reseau = models.Reseau.objects.filter(status=True)

        recettes = blog_models.Recette.objects.filter(status=True)
        recettes = recettes.filter(Q(nom__icontains=result) | Q(description__icontains=result))

        articles = organiapp_models.Article.objects.filter(status=True)
        # articles = articles.filter(nom__icontains=result)
        articles = articles.filter(Q(nom__icontains=result) | Q(description__icontains=result))


        datas={
            'siteinfo':siteinfo,
            'reseau':reseau,
            'result':result,
            'articles':articles,
            'longeur': len(articles),
            'recettes':recettes,
            'height':len(recettes),

        }

        return render(request, 'pages/search.html', datas)
    else:
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