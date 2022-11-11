from django_filters import FilterSet

from apps.product.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('size', 'color')

