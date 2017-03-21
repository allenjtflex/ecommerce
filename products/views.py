
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from django.db.models import Q
from .models import Product


class ProductList(ListView):
    model = Product
    #queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super( ProductList, self ).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("q")
        #print( context )
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductList, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")

        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(discription__icontains = query)
            )


        return qs



class ProductDetail(DetailView):
    model = Product
