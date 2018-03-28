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


def cataloge(request):
    phones = [
        {
            'href': 'cataloge/phone.html',
            'img_src': 'img/iphone8.jpg',
            'name': 'iPhone 8 256 Gb',
        },
        {
            'href': '#',
            'img_src': 'img/iphone8.jpg',
            'name': 'iPhone 8 256 Gb',
        },
        {
            'href': '#',
            'img_src': 'img/iphone8.jpg',
            'name': 'iPhone 8 256 Gb',
        },
    ]
    products = Product.objects.all()
    context = {
        'title': 'Каталог',
        'phones': products,
    }
    return render(request, 'mainapp/cataloge.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
