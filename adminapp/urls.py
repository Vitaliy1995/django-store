"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^users/$', adminapp.users, name='users'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d)$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d)$', adminapp.user_delete, name='user_delete'),
    re_path(r'^user/up/(?P<pk>\d)$', adminapp.user_up, name='user_up'),

    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^category/create/$', adminapp.category_create, name='category_create'),
    re_path(r'^category/update/(?P<pk>\d)$', adminapp.category_update, name='category_update'),
    re_path(r'^category/delete/(?P<pk>\d)$', adminapp.category_delete, name='category_delete'),
    re_path(r'^category/up/(?P<pk>\d)$', adminapp.category_up, name='category_up'),
]

