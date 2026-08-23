// 第三方依赖
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

// 当前项目类型
import type {
    LoginPayload,
    SessionUser,
} from '../types/auth'

// 当前项目依赖
import {
    fetchCurrentUser,
    loginUser,
    logoutUser,
} from '../api/auth'


export const useAuthStore = defineStore('auth', () => {
    const currentUser = ref<SessionUser | null>(null)
    const isSessionInitialized = ref(false)

    const isAuthenticated = computed(() => currentUser.value !== null)


    async function login(loginPayload: LoginPayload): Promise<void> {
        currentUser.value = await loginUser(loginPayload)
        isSessionInitialized.value = true
    }


    async function restoreSession(): Promise<void> {
        if (isSessionInitialized.value) {
            return
        }

        try {
            currentUser.value = await fetchCurrentUser()
        } catch {
            currentUser.value = null
        } finally {
            isSessionInitialized.value = true
        }
    }


    async function logout(): Promise<void> {
        await logoutUser()

        currentUser.value = null
        isSessionInitialized.value = true
    }


    return {
        currentUser,
        isSessionInitialized,
        isAuthenticated,
        login,
        restoreSession,
        logout,
    }
})
