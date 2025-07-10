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


urlpatterns = [
    path('admin/', admin.site.urls),

    # Product app routes
    path('', include('products.urls')),
    path('products/', include('products.urls')),

    # Authentication routes
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='search'), name='logout'),
    path('accounts/', include('accounts.urls')),  # signup
    path('accounts/', include('django.contrib.auth.urls')),  # reset, change, etc.
]

from django.conf.urls import handler403
handler403 = 'django.views.defaults.permission_denied'


