# Django 依赖
from django.db import transaction

# 第三方依赖
from rest_framework import serializers

# 当前应用依赖
from products.models import Product, ProductImage
from products.services.oss_service import (
    generate_product_image_url,
    upload_product_image,
)

class ProductImageSerializer(serializers.ModelSerializer):
    """将秦商品图片模型转换成前端需要的 JSON 数据"""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image_role',
            'sort_order',
            'image_url',
        ]


    def get_image_url(self, product_image: ProductImage) -> str:
        """根据数据库中的 Object Key 生成临时访问 URL"""

        return generate_product_image_url(product_image.object_key)



class ProductListSerializer(serializers.ModelSerializer):
    """将商品转化为订购页面需要的列表数据"""

    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_category',
            'price',
            'main_image',
        ]

    def get_main_image(self, product: Product) -> dict[str, object] | None:
        """获取商品主图数据"""

        # 返回 ProductImage 或 NULL
        main_image = product.images.filter(
            image_role=ProductImage.Role.MAIN,
        ).first()

        if main_image is None:
            return None

        return ProductImageSerializer(main_image).data

class ProductPublishSerializer(serializers.ModelSerializer):
    main_image = serializers.FileField(write_only=True)
    detail_image_1 = serializers.FileField(write_only=True, required=False)
    detail_image_2 = serializers.FileField(write_only=True, required=False)
    detail_image_3 = serializers.FileField(write_only=True, required=False)
    detail_image_4 = serializers.FileField(write_only=True, required=False)
    detail_image_5 = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_category',
            'product_code',
            'price',
            'delivery_time_limit_minutes',
            'main_image',
            'detail_image_1',
            'detail_image_2',
            'detail_image_3',
            'detail_image_4',
            'detail_image_5',
        ]

    def create(self, validated_data: dict[str, object]) -> Product:
        main_image = validated_data.pop('main_image')

        detail_images = []

        for sort_order in range(1, 6):
            detail_image = validated_data.pop(
                f'detail_image_{sort_order}',
                None,
            )

            if detail_image is not None:
                detail_images.append((sort_order, detail_image))

        with transaction.atomic():
            created_product = Product.objects.create(
                published_by=self.context['request'].user,
                **validated_data
            )

            # 把商品主图上传到OSS，并接受返回的Object Key
            main_object_key = upload_product_image(
                main_image,
                created_product.id,
            )

            ProductImage.objects.create(
                product=created_product,
                object_key=main_object_key,
                image_role=ProductImage.Role.MAIN,
                sort_order=0,
            )

            for detail_sort_order, detail_image in detail_images:
                detail_object_key = upload_product_image(
                    detail_image,
                    created_product.id,
                )

                ProductImage.objects.create(
                    product=created_product,
                    object_key=detail_object_key,
                    image_role=ProductImage.Role.DETAIL,
                    sort_order=detail_sort_order,
                )

        return created_product

