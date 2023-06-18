from django.urls import path

from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]