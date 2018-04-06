from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm

# Create your views here.


def users(request):

    all_users = ShopUser.objects.all()

    context = {
        'title': 'Админка',
        'users': all_users,
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'Создание пользователя'

    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_edit.html', context)


def user_update(request, pk):
    title = 'Редактирование пользователя'
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        if request.method == 'POST':
            form = ShopUserEditForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))

        else:
            form = ShopUserEditForm(instance=user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_edit.html', context)


def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        user.is_active = False
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_up(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        user.is_active = True
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))