from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket

# Create your views here.


def main(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    else:
        basket = []
    context = {
        'title': 'Корзина',
        'basket': basket
    }
    return render(request, 'basketapp/basket.html', context)


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_object = Basket.objects.filter(user=request.user, product=product).first()
    if basket_object:
        basket_object.quantity += 1
        basket_object.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

