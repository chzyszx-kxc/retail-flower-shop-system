<template>
  <view>
    <text>商品 ID：{{ productId }}</text>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { onLoad } from '@dcloudio/uni-app'

const productId = ref('')

onLoad((query) => {
  productId.value = String(query?.id ?? '')
})
</script>