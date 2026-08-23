<template>
  <header class="admin-topbar">
    <img
        class="admin-topbar__logo"
        src="../assets/admin-layout/admin-logo.png"
    >
    <nav
      class="admin-breadcrumb"
    >
      <template
        v-for="(item, index) in breadcrumbItems" :key="item.path">
        <span v-if="index > 0" class="admin-breadcrumb__separator">&gt</span>
        <span>{{ item.meta.title }}</span>
      </template>
    </nav>

    <div class="admin-employee">
      <span class="admin-employee__divider"></span>

      <img
        class="admin-employee__avatar"
        src="../assets/admin-layout/employee-avatar.png"
      >

      <div class="admin-employee__details">
        <span class="admin-employee__name">
          {{ currentUser?.employeeName }}
        </span>
        <span class="admin-employee__job-title">
          {{ currentUser?.jobTitle }}
        </span>
      </div>

      <img
        class="admin-employee__arrow"
        src="../assets/admin-layout/employee-menu-arrow.svg"
      >
    </div>
  </header>
</template>

<script setup lang="ts">
// 第三方依赖
import {storeToRefs} from "pinia";
import { useRoute } from 'vue-router'
import { computed } from "vue";

// 当前项目依赖
import { useAuthStore } from '../stores/auth.ts'

const route = useRoute()
const { currentUser } = storeToRefs(useAuthStore())

const breadcrumbItems = computed(() => {
  return route.matched.filter((item) => item.meta.title)
})
</script>

<style scoped>
  .admin-topbar {
    display: flex;
    height: 68px;
    padding-left:31px;
    background: #f3f3f3;
  }

  .admin-topbar__logo {
    flex: 0 0 112px;
    width: 112px;
    height: 68px;
    object-fit: cover;
  }

  .admin-breadcrumb {
    display: flex;
    flex: 1;
    align-items: flex-end;
    gap: 10px;
    min-width: 0;
    height: 68px;
    padding: 0 0 9px 51px;
    font-family: STHeiti, sans-serif;
    font-size: 16px;
  }

  .admin-employee {
    display: flex;
    flex: 0 0 202px;
    height: 68px;
    font-family: "PingFang TC", sans-serif;
  }

  .admin-employee__divider {
    width: 1px;
    height: 56px;
    margin-top: 6px;
    background: #d9d9d9;
  }

  .admin-employee__avatar {
    width: 54px;
    height: 54px;
    margin: 7px 20px 0 14px;
    border-radius: 50%;
    object-fit: cover;
  }

  .admin-employee__details {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-top: 12px;
  }

  .admin-employee__name {
    color: #262626;
    font-size: 15px;
    font-weight: 600;
    line-height: 22px;
  }

  .admin-employee__job-title {
    color: #8e8e93;
    font-size: 10px;
    font-weight: 600;
    line-height: 14px;
  }

  .admin-employee__arrow {
    width: 6px;
    height: 12px;
    margin: 19px 0 0 6px;
  }
</style>