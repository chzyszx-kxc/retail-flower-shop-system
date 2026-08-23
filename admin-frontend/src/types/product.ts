import type { UploadUserFile } from 'element-plus'

// 数据库允许保存的商品类目
export type ProductCategory =
    | 'flower_bucket'
    | 'flower_box'
    | 'flower_arrangement'
    | 'hand_bouquet'
    | 'perfume'
    | 'mini_flower'
    | 'other'

// 发布商品页面的普通表单数据
export interface ProductPublishForm {
    productName: string
    productCategory: ProductCategory | undefined
    productCode: string
    price: number | undefined
    deliveryTimeLimitDays: number | undefined
}

// Element Plus 当前管理的六个图片坑位
export interface ProductPublishFiles {
    mainImageFiles: UploadUserFile[]
    detailImage1Files: UploadUserFile[]
    detailImage2Files: UploadUserFile[]
    detailImage3Files: UploadUserFile[]
    detailImage4Files: UploadUserFile[]
    detailImage5Files: UploadUserFile[]
}

// 表单校验通过后交给 API 层的数据
export interface ProductPublishPayload {
    productName: string
    productCategory: ProductCategory
    productCode: string
    price: number
    deliveryTimeLimitMinutes: number
    mainImage: File
    detailImage1?: File
    detailImage2?: File
    detailImage3?: File
    detailImage4?: File
    detailImage5?: File
}