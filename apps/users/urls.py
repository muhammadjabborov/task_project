from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import RegisterAPIView, GetUserAPIView

urlpatterns = [
    path('user/info/', GetUserAPIView.as_view(), name='get_info'),
    path('user/register/', RegisterAPIView.as_view(), name='register'),
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='login_refresh')
]
