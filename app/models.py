from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Model, DateTimeField, CharField, SlugField, TextField, ForeignKey, CASCADE, DecimalField, \
    IntegerField, TextChoices, ImageField, BooleanField
from django.utils.text import slugify
from rest_framework.fields import DateField
import datetime


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    # ARAB-TILI
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Product(BaseModel):
    class Size(TextChoices):
        S = "S"
        M = "M"
        L = "L"
        XL = "XL"
        XXL = "XXL"

    class Color(TextChoices):
        RED = "RED"
        GREEN = "GREEN"
        BLACK = "BLACK"
        WHITE = "WHITE"
        YELLOW = "YELLOW"

    title = CharField(max_length=255)
    description = RichTextField()
    category = ForeignKey(Category, CASCADE)
    price = DecimalField(max_digits=9, decimal_places=2)
    discount = IntegerField(default=0)
    count = IntegerField(default=1)
    size = CharField(max_length=25, choices=Size.choices, default=Size.S)
    color = CharField(max_length=25, choices=Color.choices, default=Color.WHITE)
    expired_date = BooleanField(default=False)

    @property
    def product_images(self):
        return self.product_images.all()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"


class ProductImage(BaseModel):
    image = ImageField(upload_to='images/')
    product = ForeignKey(Product, CASCADE, 'product_images')

    class Meta:
        db_table = 'images'
