from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404
# Create your views here.
from django.db.models import Q
from .forms import VariationInventoryFormSet
from .models import Product, Variation




class VariationList(ListView):
    model = Variation
    queryset = Variation.objects.all()
    def get_context_data(self, *args, **kwargs):
        context = super( VariationList, self ).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())

        return context

    def get_queryset(self, *args, **kwargs):

        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
            #print(queryset)
        return queryset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        #print(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                product_pk = self.kwargs.get("pk")
                product = get_object_or_404( Product, pk=product_pk)
                new_item.product = product
                new_item.save()

            messages.success(request, "Your request Success!!")
            return redirect("products")
        raise Http404






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
