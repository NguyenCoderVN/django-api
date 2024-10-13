from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_auth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('o/', include('oauth2_provider.urls')),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/token/backlist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
