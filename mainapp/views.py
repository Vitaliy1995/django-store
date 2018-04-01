from django.shortcuts import render
from mainapp.models import ProductCategory, Product
import json
import os


JSON_PATH = 'mainapp/json'

# with open(os.path.join(JSON_PATH, 'main_cataloge.json'), 'w') as outfile:
#     json.dump(cataloge, outfile, ensure_ascii=False)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


def main(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def cataloge(request, pk=None):

    links_menu = []
    products = Product.objects.all()
    all_link = {
        'pk': 0,
        'name': 'All'
    }
    links_menu.append(all_link)
    links_menu.extend(ProductCategory.objects.all())

    if pk:
        pk = int(pk)
        if pk == 0:
            pass
        else:
            products = Product.objects.filter(category__pk=pk)


    context = {
        'title': 'Каталог',
        'phones': products,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/cataloge.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
