import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Element Plus 组件正常显示所必需的基础样式
import 'element-plus/dist/index.css'

// 当前项目全局样式
import './style.css'

const app = createApp(App)

app.use(createPinia())

app.use(router)

app.use(ElementPlus)

app.mount('#app')

