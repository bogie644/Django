from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def catalog(request):
    return render(request, 'mainapp/catalog.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def molinezia(request):
    return render(request, 'mainapp/molinezia.html')

def pecilia(request):
    return render(request, 'mainapp/pecilia.html')