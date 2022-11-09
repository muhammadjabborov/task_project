from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.models import ProductImage
from app.views import CategoryModelViewSet, ProductImageAPIView, ProductModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, 'category'),
router.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
    path('images/', ProductImageAPIView.as_view())
]
