from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    return render(request, 'mainapp/index.html')

def catalog(request):

    context = {'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/catalog.html', context)

def catalog1(request):
    return render(request, 'mainapp/catalog1.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def molinezia(request):
    return render(request, 'mainapp/molinezia.html')

def pecilia(request):
    return render(request, 'mainapp/pecilia.html')

def neon(request):
    return render(request, 'mainapp/neon.html')