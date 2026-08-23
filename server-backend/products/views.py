# 第三方依赖
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

# 当前应用依赖
from products.models import Product
from products.serializers import (
    ProductListSerializer,
    ProductPublishSerializer,
)

class ProductListView(ListAPIView):
    """返回订购页面需要的已上架的商品列表"""

    queryset = Product.objects.filter(
        product_status=Product.Status.ON_SALE,
    )
    serializer_class = ProductListSerializer

class ProductPublishView(CreateAPIView):
    """接收管理端表单并发布商品"""

    # 这个View使用 ProductPublishSerializer 处理数据
    serializer_class = ProductPublishSerializer
    # 只有已经登陆的用户才能访问这个接口
    permission_classes = [IsAuthenticated]