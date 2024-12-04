from django.urls import path
from .views import ProductView , AddProduct,DetailProduct,SearchProduct

app_name = 'product'
urlpatterns = [
    path('list/', ProductView.as_view(), name='list'),
    path('add/', AddProduct.as_view(), name='add'),
    path('detail/<int:pk>', DetailProduct.as_view(), name='detail'),
    path('search/', SearchProduct.as_view(), name='detail'),
]
