from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from .models import Product


class ProductDetail( DetailView ):
    model = get_object_or_404( Product )


class ProductList( ListView ):
    model = Product
