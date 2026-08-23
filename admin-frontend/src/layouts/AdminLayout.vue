<template>
  <div class="admin-layout">
    <AdminTopbar />

    <div class="admin-layout__body">
      <AdminSidebar />

      <div class="admin-layout__content">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 当前项目依赖
import AdminSidebar from '../components/AdminSidebar.vue'
import AdminTopbar from '../components/AdminTopbar.vue'
</script>

<style scoped>
.admin-layout__body {
  display: flex;
}

.admin-layout__content {
  flex: 1;
  min-width: 0;
}
</style>