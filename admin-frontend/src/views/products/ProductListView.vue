<template>
  <main class="product-list-page">
    <el-button type="primary" @click="goToProductPublish">
      发布商品
    </el-button>
  </main>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter()

const goToProductPublish = () => {
  router.push({ name: 'ProductPublish' })
}
</script>