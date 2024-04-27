from django.urls import path
from store import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list'),
    path('materials/', views.MaterialListCreateAPIView.as_view(), name='material-list-create'),
    path('result/', views.ProductMaterialsAPIView.as_view(), name='product-materials'),
]
