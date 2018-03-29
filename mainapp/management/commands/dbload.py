from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from mainapp.views import load_from_json
from authapp.models import ShopUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            product['category'] = ProductCategory.objects.filter(name=product['category']).first()
            Product.objects.create(**product)

        ShopUser.objects.create_superuser(username='django', email='django@django.local',
                                          password='geekbrains', age=22)


