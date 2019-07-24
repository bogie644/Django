from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product



def main(request):
    return render(request, 'mainapp/index.html')

def products(request, pk=None):
    products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    if pk is not None:
        if pk:
           category = get_object_or_404(ProductCategory, pk=pk)
           products = products.filter(category=category)

        context = {'products': products, 'categories': ProductCategory.objects.all(), 'basket': basket, }
        return render(request, 'mainapp/products.html', context)

    else:
        hot_product = Product.objects.filter(is_hot=True).first()

        context = {'hot_product': hot_product, 'categories': ProductCategory.objects.all(), 'basket': basket, }
        return render(request, 'mainapp/hot_product.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')

def molinezia(request):
    return render(request, 'mainapp/molinezia.html')

def pecilia(request):
    return render(request, 'mainapp/pecilia.html')

def neon(request):
    return render(request, 'mainapp/neon.html')


# def product(request, pk = None):
#     product = product.name
#      if product.name == 'Молинезия черная':
#         return render(request, 'mainapp/molinezia.html')

