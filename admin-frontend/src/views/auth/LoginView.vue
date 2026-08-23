<template>
  <main class="login-page">
    <section class="login-visual">
      <img
          class="login-visual__image"
          src="../../assets/admin-login-visual.png"
          alt=""
      >
    </section>

    <section class="login-panel">
      <div class="login-form-frame">
        <header class="login-form-header">
          <h1 class="login-form-header__brand">LogoFlower</h1>
          <p class="login-form-header__subtitle">管理后台</p>
        </header>

        <el-form
            class="login-form"
            :model="loginForm"
            @submit.prevent="handleLogin"
        >
          <el-form-item class="login-form__item">
            <el-input
                v-model="loginForm.username"
                placeholder="账号"
                autocomplete="username"
            ></el-input>
          </el-form-item>

          <el-form-item class="login-form__item">
            <el-input
                v-model="loginForm.password"
                type="password"
                placeholder="密码"
                autocomplete="current-password"
            ></el-input>
          </el-form-item>

          <el-button
              class="login-form__submit"
              native-type="submit"
              :loading="isSubmitting"
          >
            登陆
          </el-button>
        </el-form>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
// 第三方依赖
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

// 当前项目类型
import type { LoginPayload } from '../../types/auth'

// 当前项目依赖
import { useAuthStore } from '../../stores/auth'


const router = useRouter()
const authStore = useAuthStore()

const loginForm = reactive<LoginPayload>({
  username: '',
  password: '',
})

const isSubmitting = ref(false)


async function handleLogin(): Promise<void> {
  if (isSubmitting.value) {
    return
  }

  if (loginForm.username.trim() === '' || loginForm.password === '') {
    ElMessage.warning('请输入账号和密码')
    return
  }

  isSubmitting.value = true

  try {
    await authStore.login({
      username: loginForm.username.trim(),
      password: loginForm.password,
    })

    ElMessage.success('登录成功')
    await router.push('/')
  } catch {
    ElMessage.error('账号或密码错误')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
/* 登录页由左侧视觉图和右侧表单面板组成，各占页面宽度的一半 */
.login-page {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  height: 100vh;
  background: #ffffff;
}

/* 左侧区域跟随页面高度 */
.login-visual {
  min-width: 0;
  min-height: 100vh;
}

/* 图片铺满左侧区域，超出的部分按比例裁切 */
.login-visual__image {
  display: block;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  object-fit: cover;
}

/* 使用 Flex 将表单放置在右侧区域正中央 */
.login-panel {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 0;
  padding: 40px;
  background: #ffffff;
}

/* 表单宽度来自 Figma，字体只作用于当前登录模块 */
.login-form-frame {
  width: 395px;
  max-width: 100%;
  font-family: "Kaiti SC", "KaiTi", "STKaiti", serif;
}

/* 标题与副标题居中排列 */
.login-form-header {
  text-align: center;
}

.login-form-header__brand {
  margin: 0;
  color: #000000;
  font-size: 40px;
  font-weight: 400;
  line-height: 56px;
}

.login-form-header__subtitle {
  margin: 0;
  color: #000000;
  font-size: 32px;
  font-weight: 400;
  line-height: 45px;
}

/* 标题区总高为 101px，输入框从纵坐标 127px 开始，因此间距为 26px */
.login-form {
  margin-top: 26px;
}

/* 第一个输入框与第二个输入框之间保留 29px */
.login-form__item {
  margin-bottom: 29px;
}

/* 第二个输入框与登录按钮之间保留 35px */
.login-form__item + .login-form__item {
  margin-bottom: 35px;
}

/* 修改 Element Plus 输入框内部结构，使其对应 Figma 的直角黑色边框 */
.login-form__item :deep(.el-input__wrapper) {
  height: 55px;
  padding: 0 13px;
  border-radius: 0;
  background: #ffffff;
  box-shadow: 0 0 0 1px #000000 inset;
}

/* 鼠标经过和获得焦点时仍然维持原设计的黑色边框 */
.login-form__item :deep(.el-input__wrapper:hover),
.login-form__item :deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px #000000 inset;
}

/* 设置输入内容和占位文字的字体 */
.login-form__item :deep(.el-input__inner) {
  height: 45px;
  color: #000000;
  font-family: inherit;
  font-size: 32px;
  font-weight: 400;
  line-height: 45px;
}

.login-form__item :deep(.el-input__inner::placeholder) {
  color: #000000;
  opacity: 1;
}

/* 登录按钮使用 Figma 中的黑底、白字和直角设计 */
.login-form__submit {
  width: 100%;
  height: 56px;
  padding: 0;
  border: 1px solid #000000;
  border-radius: 0;
  color: #ffffff;
  background: #000000;
  font-family: inherit;
  font-size: 32px;
  font-weight: 400;
  line-height: 45px;
}

/* 避免 Element Plus 在交互状态下自动改变按钮配色 */
.login-form__submit:hover,
.login-form__submit:focus,
.login-form__submit:active {
  border-color: #000000;
  color: #ffffff;
  background: #000000;
}
</style>
