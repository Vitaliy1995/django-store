from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryEditForm

# Create your views here.


@user_passes_test(lambda x: x.is_superuser)
def users(request):

    all_users = ShopUser.objects.all()

    context = {
        'title': 'Пользователи',
        'users': all_users,
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    title = 'Создание пользователя'

    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))

    else:
        form = ShopUserRegisterForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_edit.html', context)


@user_passes_test(lambda x: x.is_superuser)
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


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        user.is_active = False
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def user_up(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        user.is_active = True
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    all_categories = ProductCategory.objects.all()

    context = {
        'title': 'Категории',
        'categories': all_categories,
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda x: x.is_superuser)
def category_create(request):
    title = 'Создание категории'

    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryEditForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/category_edit.html', context)


@user_passes_test(lambda x: x.is_superuser)
def category_update(request, pk):
    title = 'Редактирование категории'
    category = get_object_or_404(ProductCategory, pk=int(pk))
    if category:
        if request.method == 'POST':
            form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:categories'))

        else:
            form = ProductCategoryEditForm(instance=category)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/category_edit.html', context)


@user_passes_test(lambda x: x.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=int(pk))
    if category:
        category.active = False
        category.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def category_up(request, pk):
    category = get_object_or_404(ProductCategory, pk=int(pk))
    if category:
        category.active = True
        category.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))