from django_filters import FilterSet

from app.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('size', 'color')

