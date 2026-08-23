// 当前项目类型
import type {
    LoginPayload,
    SessionUser,
    SessionUserResponse,
} from '../types/auth'

// 当前项目依赖
import httpClient from './http'


function convertSessionUser(response: SessionUserResponse): SessionUser {
    return {
        id: response.id,
        username: response.username,
        employeeName: response.employee_name,
        jobTitle: response.job_title,
    }
}


async function fetchCsrfCookie(): Promise<void> {
    await httpClient.get('/auth/csrf/')
}


export async function loginUser(
    loginPayload: LoginPayload,
): Promise<SessionUser> {
    await fetchCsrfCookie()

    const response = await httpClient.post<SessionUserResponse>(
        '/auth/login/',
        loginPayload,
    )

    return convertSessionUser(response.data)
}


export async function fetchCurrentUser(): Promise<SessionUser> {
    const response = await httpClient.get<SessionUserResponse>('/auth/me/')

    return convertSessionUser(response.data)
}


export async function logoutUser(): Promise<void> {
    await httpClient.post('/auth/logout/')
}
