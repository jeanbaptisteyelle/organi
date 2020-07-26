from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, get_object_or_404
from . import views
from . import models
from website import models as website_models
from organiapp import models as organiapp_models


# Create your views here.
def blog(request):
    recette = models.Recette.objects.filter(status=True)
    recette_list = models.Recette.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recette_list, 4)
    try:
        recette = paginator.page(page)
    except PageNotAnInteger:
        recette = paginator.page(1)
    except EmptyPage:
        recette= paginator.page(paginator.num_pages)





    articles = organiapp_models.Article.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    reseau = website_models.Reseau.objects.filter(status=True)
    new = models.Recette.objects.filter(status=True).order_by('-date_update')[:3]

    datas = {
        'articles':articles,
        'siteinfo':siteinfo,
        'reseau':reseau,
        'new':new,
        'recette':recette,
        


    
    }
    return render(request, 'pages/blog.html', datas)

def blog_details(request, slug):
    tag = models.Tag.objects.filter(status=True)
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
        'tag':tag,
        
    }
    return render(request, 'pages/blog-details.html', datas)

