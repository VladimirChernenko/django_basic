from django.shortcuts import render
from .models import Category, Product


def index(request):
    return render(request, 'mainapp/index.html', context={'products': Product.objects.all()[:2]})


def products(request):
    return render(request, 'mainapp/products.html', context={'category': Category.objects.all()})


def products_list(request, pk):
    return render(request, 'mainapp/products.html', context={'category': Category.objects.all()})


def contact(request):
    return render(request, 'mainapp/contact.html')
