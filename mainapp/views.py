from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def cataloge(request):
    return render(request, 'mainapp/cataloge.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
