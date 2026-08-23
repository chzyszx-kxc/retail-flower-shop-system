export type ProductCategory =
    | 'flower_bucket'
    | 'flower_box'
    | 'flower_arrangement'
    | 'hand_bouquet'
    | 'perfume'
    | 'mini_flower'
    | 'other'

export interface ProductMainImage {
    image_url: string
}

export interface ProductListItem {
    id: number
    product_category: ProductCategory
    price: string
    main_image: ProductMainImage
}