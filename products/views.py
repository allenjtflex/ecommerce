from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from .models import Product


class ProductList(ListView):
    model = Product
    #queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super( ProductList, self ).get_context_data(*args, **kwargs)
        #print( context )
        return context


class ProductDetail(DetailView):
    model = Product
