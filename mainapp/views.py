from django.shortcuts import render
import datetime


def main(request):
    date = datetime.datetime.now()
    context = {
        'title': 'Главная',
        'date': date.strftime("%d-%m-%Y %H:%M"),
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
    context = {
        'title': 'Каталог',
        'phones': phones,
    }
    return render(request, 'mainapp/cataloge.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
