# 第三方依赖
from django.urls import path

# 当前应用依赖
from products.views import ProductListView, ProductPublishView

app_name = 'products'

urlpatterns = [
    path(
        '',
        ProductListView.as_view(),
        name="product-list",
    ),

    path(
        'publish/',
        ProductPublishView.as_view(),
        name="product-publish",
    )
]
