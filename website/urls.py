from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),

    path('newletter', views.newletter, name='newletter'),

    path('register', views.register, name='register'),

    path('login', views.login_log, name='login'),

    path('logout', views.deconnexion, name='logout'),
]