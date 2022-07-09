from unicodedata import name
from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from django.contrib.auth.models import User
import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file):
    with open(os.path.join(JSON_PATH, file + '.json')) as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

    super_user = User.objects.create_superuser(
        'django', 'chernenkomain@gmail.com', 'geekbrains', age=29)
