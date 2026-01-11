"""
URL configuration for ecocart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomLoginView
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    # Product app routes
    path('', include('products.urls')),
    # path('products/', include('products.urls')),

    # Authentication routes
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='search'), name='logout'),
    path('accounts/', include('accounts.urls')),  # signup
    path('accounts/', include('django.contrib.auth.urls')),  # reset, change, etc.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf.urls import handler403
handler403 = 'django.views.defaults.permission_denied'


