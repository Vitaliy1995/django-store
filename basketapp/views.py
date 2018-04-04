from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
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


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.filter(pk=int(pk)).first()

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket = request.user.basket.all().order_by('product__category')

        context = {
            'basket': basket,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', context)

        return JsonResponse({'result': result})


@login_required
def basket_buy(request):
    if request.method == 'POST':

        products = request.POST.keys()
        products_list = list(Product.objects.all())
        names = []
        for i in range(len(products_list)):
            names.append(products_list[i].name)
        print(names)
        for product in products:
            if product in names:
                print(product)
                new_item = Product.objects.filter(name=product).first()
                new_item.quantity -= int(request.POST[product])
                new_item.save()

        basket = Basket.objects.all()
        basket.delete()
        return HttpResponseRedirect(reverse('main'))

