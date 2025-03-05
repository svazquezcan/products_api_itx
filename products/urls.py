from django.urls import path
from .views import SimilarProductsView

urlpatterns = [
    path('<str:productId>/similar', SimilarProductsView.as_view(), name='product-similar'),
]