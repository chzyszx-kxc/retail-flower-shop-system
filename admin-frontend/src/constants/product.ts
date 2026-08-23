import type { ProductCategory } from '../types/product'

export const PRODUCT_CATEGORY_OPTIONS: Array<{
    label: string
    value: ProductCategory
}> = [
    {
        label: '抱抱桶',
        value: 'flower_bucket'
    },
    {
        label: '花盒',
        value: 'flower_box'
    },
    {
        label: '插花',
        value: 'flower_arrangement',
    },
    {
        label: '手捧花',
        value: 'hand_bouquet',
    },
    {
        label: '香水',
        value: 'perfume',
    },
    {
        label: '小鼻嘎花',
        value: 'mini_flower',
    },
    {
        label: '其他',
        value: 'other',
    },
]