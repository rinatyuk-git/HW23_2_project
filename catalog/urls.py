from django.urls import path
from catalog.views import home, contacts, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
	path('', home, name='home'),
	path('contacts/', contacts, name='contacts'),
	path('product_view/', ProductListView.as_view(), name='product_view'),
	path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
