import {
    createRouter,
    createWebHistory,
    type RouteRecordRaw
} from 'vue-router'

import { useAuthStore } from "../stores/auth.ts";

// 管理后台的页面路由
const routes: RouteRecordRaw[] = [
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/auth/LoginView.vue')
    },
    {
        path: '/',
        component: () => import('../layouts/AdminLayout.vue'),
        children: [
            {
                path: '',
                name: 'home',
                component: () => import('../views/home/AdminHomeView.vue'),
                meta: {
                    title: '快速操作',
                    showInSidebar: true,
                    sidebarIcon: 'quick-operation'
                },
            },
            {
                path: '/products',
                meta: {
                    title: '花礼上下架',
                    showInSidebar: true,
                    sidebarIcon: 'product-management'
                },
                children: [
                    {
                        path: '',
                        name: 'ProductList',
                        component: () => import('../views/products/ProductListView.vue')
                    },
                    {
                        path: 'publish',
                        name: 'ProductPublish',
                        component: () => import('../views/products/ProductPublishView.vue'),
                        meta: {
                            title: '发布商品'
                        }
                    }
                ]
            }
        ],
    },
]

// 创建管理端路由实例
const router = createRouter({
    // 使用 URL 路径，并自动读取 Vite 的部署基础路径
    history: createWebHistory(import.meta.env.BASE_URL),

    // 后续在这里加入登录页和管理后台页面
    routes,
})

// 统一管理ToB端后台的登陆状态
router.beforeEach(async (to) => {
    const authStore = useAuthStore()

    await authStore.restoreSession()

    if (!authStore.isAuthenticated && to.name !== 'login') {
        return { name: 'login' }
    }

    if (authStore.isAuthenticated && to.name === 'login') {
        return { name: 'home' }
    }
})

export default router