<template>
  <!-- 商品主图，点击后进入对应商品详情页 -->
  <image
      class="product-cover"
      :src="props.mainImageUrl"
      mode="aspectFill"
      @click="goToProductDetail"
  />
</template>

<script setup lang="ts">
// 商品主图展示与跳转需要的数据
const props = defineProps<{
  productId: number
  mainImageUrl: string
}>()

// 根据商品 ID 进入对应商品详情页
function goToProductDetail(): void {
  uni.navigateTo({
    url: `/pages/product-detail/product-detail?id=${props.productId}`,
  })
}
</script>

<style scoped>
/* Figma 商品主图尺寸 */
.product-cover {
  display: block;
  width: 292rpx;
  height: 311rpx;
  border-radius: 23rpx;
}
</style>