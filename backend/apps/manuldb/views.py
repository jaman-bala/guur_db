from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .weapons import Weapons
from .products import Product


class WeaponsView(ListView):
        model = Weapons
        template_name = 'weapons.html'
        context_object_name = 'weapons'
        paginate_by = 70
        queryset = Weapons.objects.all()


class WeaponsDetailView(DetailView):
        model = Weapons
        template_name = 'details_weapons.html'
        context_object_name = 'weaponsout'
        queryset = Weapons.objects.all()


class ProductView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 70
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_products.html'
    context_object_name = 'productsout'
    queryset = Product.objects.all()