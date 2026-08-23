// 第三方依赖
import axios from 'axios'

const httpClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_PATH,
    withCredentials: true,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
})

export default httpClient
