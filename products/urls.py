from django.urls import path
from . import views
from django.urls import path, include





urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('search/', views.search_product, name='search'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
   
]
