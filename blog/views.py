from django.shortcuts import render, get_object_or_404
from . import views
from . import models
from website import models as website_models
from organiapp import models as organiapp_models


# Create your views here.
def blog(request):
    articles = organiapp_models.Article.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)
    new = models.Recette.objects.filter(status=True).order_by('-date_update')[:3]
    recette = models.Recette.objects.filter(status=True)[:6]

    datas = {
        'articles':articles,
        'siteinfo':siteinfo,
        'reseau':reseau,
        'new':new,
        'recette':recette,

    
    }
    return render(request, 'pages/blog.html', datas)

def blog_details(request, slug):
    articles = organiapp_models.Article.objects.filter(status=True)
    blog = models.Recette.objects.get(slug=slug)
    reseau = website_models.Reseau.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    blog_detail = get_object_or_404(models.Recette, slug=slug)
    recette = models.Recette.objects.filter(status=True)[:3]
    sign = models.Recette.objects.filter(status=True)[:1]
    catego = models.Recette.objects.filter(status=True)[:1]


    datas = {
        'articles':articles,
        "siteinfo":siteinfo,
        "reseau":reseau,
        'blog':blog,
        'blog_detail':blog_detail,
        'recette':recette,
        'sign':sign,
        'catego':catego,
        
    }
    return render(request, 'pages/blog-details.html', datas)

