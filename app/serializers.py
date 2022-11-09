from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from app.models import Category, ProductImage, Product


class CategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError("This category name is already taken")
        return data

    class Meta:
        model = Category
        exclude = ('slug',)


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ProductImageModelSerializer(instance.product_images.first()).data
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent

    class Meta:
        model = Product
        fields = '__all__'
