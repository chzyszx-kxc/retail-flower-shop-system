# 标准库依赖
from datetime import timedelta
from pathlib import Path
from uuid import uuid4

# 第三方依赖
import alibabacloud_oss_v2 as oss
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile


def create_oss_client() -> oss.Client:
    """根据 Django 配置创建 OSS 客户端"""

    credentials_provider = oss.credentials.StaticCredentialsProvider(
        settings.OSS_ACCESS_KEY_ID,
        settings.OSS_ACCESS_KEY_SECRET,
    )

    # 加载 SDK 默认配置
    config = oss.config.load_default()

    # 设置访问 OSS 所需身份、地域和服务地址
    config.credentials_provider = credentials_provider
    config.region = settings.OSS_REGION
    config.endpoint = f'https://{settings.OSS_ENDPOINT}'

    return oss.Client(config)


def upload_product_image(file: UploadedFile, product_id: int) -> str:
    """将商品图片上传到 OSS，并返回数据库需要保存的 Object Key"""

    # 保留原图片的扩展名
    file_suffix = Path(file.name).suffix.lower()

    # 使用商品 ID 分类，并通过 UUID 避免文件重名
    object_key = f'products/{product_id}/{uuid4().hex}{file_suffix}'

    client = create_oss_client()

    client.put_object(
        oss.PutObjectRequest(
            bucket=settings.OSS_BUCKET_NAME,
            key=object_key,
            body=file.file,
            content_type=file.content_type,
            content_length=file.size,
        )
    )

    return object_key


def delete_product_image(object_key: str) -> None:
    """根据 Object Key 删除 OSS 中的商品图片"""

    client = create_oss_client()

    client.delete_object(
        oss.DeleteObjectRequest(
            bucket=settings.OSS_BUCKET_NAME,
            key=object_key,
        )
    )


def generate_product_image_url(
    object_key: str,
    expires_minutes: int = 15,
) -> str:
    """根据 Object Key 生成商品图片的临时访问 URL"""

    client = create_oss_client()

    # presign() 为 OSS 文件生成一个有实效的签名访问URL
    result = client.presign(
        oss.GetObjectRequest(
            bucket=settings.OSS_BUCKET_NAME,
            key=object_key,
        ),
        expires=timedelta(minutes=expires_minutes),
    )

    return result.url