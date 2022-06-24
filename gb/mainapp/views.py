from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
        ]

    content = {'links_menu': links_menu}
    return render(request, 'mainapp/products.html', context=content)

def contact(request):
    return render(request, 'mainapp/contact.html')