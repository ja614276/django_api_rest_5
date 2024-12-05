from django.urls import path

from django_api.views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(),name='product_list'),
    path('products/<int:id>', ProductView.as_view(), name='product_list_id')
]