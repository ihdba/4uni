from django.urls import path

from .views import AddProductView
from . import views

urlpatterns = [
    #path('', eshop, name = 'eshop'),
    #path('', Eshop, name = 'eshop'),
    # path('product_list', ProductList, name = 'product_list'),
    path('add_product', AddProductView.as_view(), name = 'add_product'),
    # path('supplier', SupplierPageView.as_view(), name = 'supplier'),
    # path('add_supplier', AddSupplierView.as_view(), name = 'add_supplier'),
    # path('<str:pk>/product_update', ProductUpdateView.as_view(), name = 'product_update'),
    path('', views.ProductList, name = 'eshop'),
    path('<str:pk>/', views.ProductDetail, name = 'product_detail'),
    path('<str:pk>/delete', views.ProductDelete, name = 'delete_product'),

]