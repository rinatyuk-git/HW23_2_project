from django.urls import path
from catalog.views import (
    home,
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_view/", ProductListView.as_view(), name="product_view"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
