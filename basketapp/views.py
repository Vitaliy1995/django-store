from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from mainapp.models import Product
from basketapp.models import Basket

# Create your views here.


@login_required
def main(request):
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    else:
        basket = []
    context = {
        'title': 'Корзина',
        'basket': basket,
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('cataloge:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    basket_object = Basket.objects.filter(user=request.user, product=product).first()
    if basket_object:
        basket_object.quantity += 1
        basket_object.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def product_del(request, pk):
    # Следует подтверждение вызывать
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
