<template>
  <div class="admin-sidebar">
    <!--
      先读取当前菜单的 item.path
          ↓
      item.path 是否等于空字符串？
         ↙ 是              ↘ 否
      当前地址是否为 /     当前地址是否以 item.path 开头？
         ↓                   ↙
      得到 true 或 false
          ↓
      true：添加选中样式类
      false：不添加
    -->
    <div
      v-for="item in sidebarItems" :key="item.path"
      class="admin-sidebar__item"
      :class="{
        'admin-sidebar__item--active':
          item.path === '' ? route.path === '/' : route.path.startsWith(item.path)
      }"
      @click="router.push(item.path || '/')"
    >
      <img
          class="admin-sidebar__icon"
          :src="sidebarIcons[item.meta?.sidebarIcon ?? '']"
      >
      <span>{{ item.meta?.title }}</span>
    </div>

  </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'

// 当前项目依赖
import quickOperationIcon from '../assets/admin-layout/quick-operation.svg'
import productManagementIcon from '../assets/admin-layout/product-management.svg'

const route = useRoute()
const router = useRouter()

const sidebarIcons: Record<string, string> = {
  'quick-operation': quickOperationIcon,
  'product-management': productManagementIcon,
}

const sidebarItems = router.options.routes
  .find((item) => item.path === '/')
  ?.children
  ?.filter((item) => item.meta?.showInSidebar)
</script>

<style scoped>
.admin-sidebar {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex-shrink: 0;
  width: 194px;
  min-height: calc(100vh - 68px);
  background: #f3f3f3;
}

.admin-sidebar::before {
  content: '';
  height: 1px;
  margin: 0 10px;
  background: #cfcfcf;
}

.admin-sidebar__item {
  position: relative;
  display: flex;
  align-items: center;
  gap: 9px;
  width: 160px;
  height: 36px;
  margin-left: 17px;
  padding: 0 13px;
  border-radius: 18px;
  color: #565656;
  font-family: STHeiti, sans-serif;
  font-size: 13px;
  line-height: 13px;
  cursor: pointer;
}

.admin-sidebar__item--active::before {
  content: '';
  position: absolute;
  top: 0;
  left: -17px;
  width: 8px;
  height: 36px;
  border-radius: 0 8px 8px 0;
  background: #656854;
}

.admin-sidebar__icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
}

.admin-sidebar__item--active {
  color: #ffffff;
  background: #696653;
}

.admin-sidebar__item--active .admin-sidebar__icon {
  filter: brightness(0) invert(1);
}
</style>