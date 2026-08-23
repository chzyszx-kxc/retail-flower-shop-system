# Django 依赖
from django.conf import settings
from django.db import models


# region Product商品元信息模型
class Product(models.Model):

    # 商品分类
    class Category(models.TextChoices):
        FLOWER_BUCKET = 'flower_bucket', '抱抱桶'
        FLOWER_BOX ="flower_box", '花盒'
        FLOWER_ARRANGEMENT = 'flower_arrangement', '花艺'
        HAND_BOUQUET = 'hand_bouquet', '手捧花'
        PERFUME = 'perfume', '香水'
        MINI_FLOWER = 'mini_flower', '小鼻嘎花'
        OTHER = 'other', '其它'

    # 商品当前的上下架状态
    class Status(models.TextChoices):
        ON_SALE = 'on_sale', '已上架'
        OFF_SALE = 'off_sale', '已下架'

    # 商品ID
    id = models.AutoField(primary_key=True)

    # 商品基本信息
    # product_code是给人看的产品编号
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(
        max_length=18,
        choices=Category.choices
    )

    # 商品销售信息
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time_limit_minutes = models.PositiveIntegerField()
    product_status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ON_SALE
    )

    # 商品发布信息
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='published_products'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 明确指定表名，避免使用Django默认的products_product
        db_table = 'product'

        # 查询时默认让新商品排在前面，ID越大表示创建时间越晚
        ordering = ['-id']

    def __str__(self) -> str:
        return self.product_name

# endregion

# region ProductImage 商品图片模型
class ProductImage(models.Model):
    class Role(models.TextChoices):
        MAIN = 'main', '主图'
        DETAIL = 'detail', '详情图'

    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        # 设置反向查询
        related_name="images",
    )

    # OSS Object Key
    object_key = models.CharField(max_length=255, unique=True)

    image_role = models.CharField(
        max_length=6,
        choices=Role.choices,
    )

    # sort_order标识主图与详情图，主图使用 0， 详情图依次使用 1~5
    sort_order = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'product_image'
        ordering = ['sort_order']

        constraints = [
            # 同一商品不能在同一个图片位置保存两条记录
            models.UniqueConstraint(
                fields=['product', 'sort_order'],
                name='unique_product_image_sort_order'
            ),

            # 图片的位置sort只能是 0 ~ 5
            models.CheckConstraint(
                condition=models.Q(sort_order__lte=5),
                name='product_image_sort_order_lte_check'
            )
        ]

    def __str__(self) -> str:
        return f'{self.product.product_code} - 图片 {self.sort_order}'

# endregion
