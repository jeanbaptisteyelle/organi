from django.urls import path
from . import views
urlpatterns = [
    path('', views.checkout, name='checkout'),

    path('shop-details', views.shop_details, name='shop-details'),
    
    path('shop-grid', views.shop_grid, name='shop-grid'),

    path('shoping-cart', views.shoping_cart, name='shoping-cart'),

    path('shop_details/<slug>', views.shop_details, name="shop_details"),
]