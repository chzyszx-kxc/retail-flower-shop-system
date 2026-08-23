<template>
  <view class="order-page">
    <!-- 横向滚动的商品分类栏 -->
    <scroll-view
      class="product-category"
      scroll-x
      :show-scrollbar="false"
      :scroll-left="productCategoryScrollLeft"
      @scroll="updateProductCategoryScrollLeft"
      @mousedown="startProductCategoryDrag"
      @mousemove="moveProductCategoryDrag"
      @mouseup="stopProductCategoryDrag"
      @mouseleave="stopProductCategoryDrag"
    >
      <view class="product-category-list">
        <!-- 每个分类负责显示图标、名称和单选点击 -->
        <view
          v-for="productCategory in PRODUCT_CATEGORIES"
          :key="productCategory.value"
          class="product-category__item"
          @click="selectProductCategory(productCategory.value)"
        >
          <image
              class="product-category__image"
              :src="productCategory.imageUrl"
              mode="aspectFit"
          />

          <text
              class="product-category__label"
              :class="{
                'product-category__label--selected':
                  selectCategory === productCategory.value,
              }"
          >
            {{ productCategory.label }}
          </text>
        </view>
      </view>
    </scroll-view>

    <!-- 展示当前分类和可见商品数量 -->
    <view class="product-list-heading">
      <text class="product-list-heading__explore">
        Explore
      </text>
      <text class="product-list-heading__category">
        {{ selectCategory }}
      </text>
      <view class="product-list-heading__count">
        <text class="product-list-heading__count-text">
          {{ visibleProducts.length }}
        </text>
        <text class="product-list-heading__count-text">
          items
        </text>
      </view>
    </view>

    <!-- 当前分类没有商品时只显示简单文字 -->
    <text
        v-if="visibleProducts.length === 0"
        class="product-list__empty"
    >
      暂无商品
    </text>

    <!-- 商品按照数组下标交替进入左右两列 -->
    <view
        v-else
        class="product-list"
    >
      <!-- 最新商品从左列顶部开始排列 -->
      <view class="product-list__column">
        <view
            v-for="product in leftProducts"
            :key="product.id"
            class="product-card"
        >
          <ProductCover
              :product-id="product.id"
              :main-image-url="product.main_image.image_url"
          />

          <view class="product-card__footer">
            <text class="product-card__price">
              ¥{{ product.price }}
            </text>

            <!-- 暂无点击功能的加号占位 -->
            <view class="product-card__add"></view>
          </view>
        </view>
      </view>

      <!-- 第二个商品从右列顶部开始排列 -->
      <view class="product-list__column">
        <view
            v-for="product in rightProducts"
            :key="product.id"
            class="product-card"
        >
          <ProductCover
              :product-id="product.id"
              :main-image-url="product.main_image.image_url"
          />

          <view class="product-card__footer">
            <text class="product-card__price">
              ¥{{ product.price }}
            </text>

            <!-- 暂无点击功能的加号占位 -->
            <view class="product-card__add"></view>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import type {ProductCategory, ProductListItem} from '@/types/product'
import { ref, computed } from 'vue'
import { onShow } from '@dcloudio/uni-app'
import ProductCover from "@/component/ProductCover.vue";

// “全部分类”是页面筛选值，不是后端商品分类，所以这里要单独加上
type ProductCategoryFilter = ProductCategory | 'all'

interface ProductCategoryOption {
  label: string
  value: ProductCategoryFilter
  imageUrl:string
}

// 分类栏
const PRODUCT_CATEGORIES: ProductCategoryOption[] = [
  {
    label: '全部分类',
    value: 'all',
    imageUrl: '/static/order/categories/category-all.png',
  },
  {
    label: '抱抱桶',
    value: 'flower_bucket',
    imageUrl: '/static/order/categories/category-flower-bucket.png',
  },
  {
    label: '花盒',
    value: 'flower_box',
    imageUrl: '/static/order/categories/category-flower-box.png',
  },
  {
    label: '插花',
    value: 'flower_arrangement',
    imageUrl: '/static/order/categories/category-flower-arrangement.png',
  },
  {
    label: '手捧花',
    value: 'hand_bouquet',
    imageUrl: '/static/order/categories/category-hand-bouquet.png',
  },
  {
    label: '香水',
    value: 'perfume',
    imageUrl: '/static/order/categories/category-perfume.png',
  },
  {
    label: '小鼻嘎花',
    value: 'mini_flower',
    imageUrl: '/static/order/categories/category-mini-flower.png',
  },
  {
    label: '其它',
    value: 'other',
    imageUrl: '/static/order/categories/category-other.png',
  },
]

// 默认单选“全部分类”
const selectCategory = ref<ProductCategoryFilter>('all')

// H5 隐藏滚动条后，保留鼠标拖动能力
const productCategoryScrollLeft = ref(0)
let productCategoryDragStartX = 0
let productCategoryDragStartScrollLeft = 0
let isProductCategoryDragging = false
let productCategoryHasDragged = false

function updateProductCategoryScrollLeft(
    event: { detail: { scrollLeft: number } }
): void {
  productCategoryScrollLeft.value = event.detail.scrollLeft
}

function startProductCategoryDrag(event: MouseEvent): void {
  isProductCategoryDragging = true
  productCategoryHasDragged = false
  productCategoryDragStartX = event.clientX
  productCategoryDragStartScrollLeft = productCategoryScrollLeft.value
}

function moveProductCategoryDrag(event: MouseEvent): void {
  if (!isProductCategoryDragging) {
    return
  }

  const dragDistance = event.clientX - productCategoryDragStartX

  if (Math.abs(dragDistance) > 3) {
    productCategoryHasDragged = true
  }

  productCategoryScrollLeft.value =
      productCategoryDragStartScrollLeft - dragDistance
}

function stopProductCategoryDrag(): void {
  isProductCategoryDragging = false

  setTimeout(() => {
    productCategoryHasDragged = false
  })
}

function selectProductCategory(
    productCategory: ProductCategoryFilter
): void {
  if (productCategoryHasDragged) {
    return
  }

  selectCategory.value = productCategory
}

// 商品列表
let productListUrl = `${import.meta.env.VITE_API_BASE_PATH}/products/`

// #ifdef MP-WEIXIN
productListUrl = `${import.meta.env.VITE_API_ORIGIN}${productListUrl}`
// #endif

// 已上架的商品
const allProducts = ref<ProductListItem[]>([])

// 根据当前分类得到需要展示的商品
const visibleProducts = computed(() => {
  if (selectCategory.value === 'all') {
    return allProducts.value
  }

  return allProducts.value.filter(
      (product) => {
        return product.product_category === selectCategory.value
      }
  )
})

// 数组第 1、3、5 个商品进入左列
const leftProducts = computed<ProductListItem[]>(() =>
    visibleProducts.value.filter(
        (_, index) => index % 2 === 0,
    ),
)

// 数组第 2、4、6 个商品进入右列
const rightProducts = computed<ProductListItem[]>(() =>
    visibleProducts.value.filter(
        (_, index) => index % 2 === 1,
    ),
)

// 请求订购页面需要的商品
function getProducts(): void {
  uni.request({
    url: productListUrl,

    success(response) {
      allProducts.value = response.data as ProductListItem[]
    },
  })
}

onShow(getProducts)
</script>

<style scoped>
/* 当前分类和可见商品数量 */
.product-list-heading {
  display: flex;
  flex-direction: column;
  width: 630rpx;
  height: 244rpx;
  margin: 42rpx 0 0 63rpx;
  overflow: visible;
}

/* 固定显示的Explore标题 */
.product-list-heading__explore {
  display: block;
  flex: none;
  width: 437rpx;
  height: 101rpx;
  color: #000000;
  font-family: "Hiragino Mincho Pro", serif;
  font-size: 92rpx;
  font-weight: 300;
  line-height: 101rpx;
  white-space: nowrap;
}

/* 跟随当前单选值变化的分类名 */
.product-list-heading__category {
  display: block;
  align-self: flex-start;
  flex: none;
  color: #000000;
  font-family: "Hiragino Mincho Pro", serif;
  font-size: 69rpx;
  font-weight: 300;
  line-height: 82rpx;
  white-space: nowrap;
}

/* 固定在标题板块右侧的商品数量 */
.product-list-heading__count {
  display: flex;
  flex: none;
  width: 100%;
  padding-right: 57rpx;
  box-sizing: border-box;
  justify-content: flex-end;
  align-items: center;
  gap: 19rpx;
}

/* 数量和items使用相同文字样式 */
.product-list-heading__count-text {
  color: #000000;
  font-family: "Noto Sans SC", sans-serif;
  font-size: 38rpx;
  font-weight: 400;
  line-height: 46rpx;
  white-space: nowrap;
}

/* 订购页面背景与顶部空间 */
.order-page {
  min-height: 100vh;
  padding-top: 118rpx;
  box-sizing: border-box;
  background-color: #f9f9f9;
}

/* 横向滚动的商品分类栏 */
.product-category {
  display: block;
  width: 708rpx;
  height: 137rpx;
  margin: 0 auto;
  white-space: nowrap;
}

/* 所有分类横向排列 */
.product-category-list {
  display: inline-flex;
  padding: 4rpx 36rpx 0;
  gap: 50rpx;
  box-sizing: border-box;
}

/* 单个分类的图片和名称 */
.product-category__item {
  flex: none;
  width: 99rpx;
  text-align: center;
}

/* 4倍导出的分类图片按52px显示 */
.product-category__image {
  display: block;
  width: 99rpx;
  height: 99rpx;
}

/* 未选中的分类名称 */
.product-category__label {
  display: block;
  height: 23rpx;
  color: #8e8e93;
  font-family: "Noto Sans SC", sans-serif;
  font-size: 19rpx;
  line-height: 23rpx;
  text-align: center;
  white-space: nowrap;
}

/* 当前单选分类的名称 */
.product-category__label--selected {
  color: #000000;
}

/* 商品列表横向分为两列，并向上覆盖标题区域 */
.product-list {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: flex-start;
  width: 630rpx;
  margin-left: 63rpx;
  gap: 46rpx;
  transform: translateY(-38rpx);
}

/* 每列宽度与商品主图一致 */
.product-list__column {
  flex: none;
  width: 292rpx;
}

/* 右列从第二个商品的位置开始 */
.product-list__column:nth-child(2) {
  margin-top: 78rpx;
}

/* 单个商品保持设计稿中的固定排列高度 */
.product-card {
  width: 292rpx;
  height: 422rpx;
}

/* 价格和加号占位横向排列 */
.product-card__footer {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  height: 95rpx;
  margin-top: 15rpx;
  padding: 0 23rpx 0 13rpx;
  box-sizing: border-box;
}

/* 商品价格 */
.product-card__price {
  color: #000000;
  font-family: Cambay, sans-serif;
  font-size: 38rpx;
  font-weight: 400;
  line-height: 46rpx;
  white-space: nowrap;
}

/* 暂无点击功能的加号占位 */
.product-card__add {
  position: relative;
  flex: none;
  width: 46rpx;
  height: 46rpx;
}

/* 用两条线组成加号 */
.product-card__add::before,
.product-card__add::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 27rpx;
  height: 3rpx;
  background-color: #000000;
  transform: translate(-50%, -50%);
}

.product-card__add::after {
  transform: translate(-50%, -50%) rotate(90deg);
}
</style>
