// 商品 API

// 当前项目类型
import type { ProductPublishPayload } from "../types/product";

// 当前项目依赖
import httpClient from './http'

export async function publishProduct(
    payload: ProductPublishPayload,
): Promise<void> {
    const formData = new FormData()

    formData.append('product_name', payload.productName)
    formData.append('product_category', payload.productCategory)
    formData.append('product_code', payload.productCode)
    formData.append('price', payload.price.toString())
    formData.append(
        'delivery_time_limit_minutes',
        payload.deliveryTimeLimitMinutes.toString(),
    )
    formData.append('main_image', payload.mainImage)

    if (payload.detailImage1) {
        formData.append('detail_image_1', payload.detailImage1)
    }

    if (payload.detailImage2) {
        formData.append('detail_image_2', payload.detailImage2)
    }

    if (payload.detailImage3) {
        formData.append('detail_image_3', payload.detailImage3)
    }

    if (payload.detailImage4) {
        formData.append('detail_image_4', payload.detailImage4)
    }

    if (payload.detailImage5) {
        formData.append('detail_image_5', payload.detailImage5)
    }

    await httpClient.post('/products/publish/', formData)
}