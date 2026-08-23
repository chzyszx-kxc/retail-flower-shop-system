// 登录接口需要接收的数据
export interface LoginPayload {
    username: string
    password: string
}

// Django 接口返回的原始员工数据
export interface SessionUserResponse {
    id: number
    username: string
    employee_name: string
    job_title: string
}

// 管理前端内部使用的当前员工数据
export interface SessionUser {
    id: number
    username: string
    employeeName: string
    jobTitle: string
}
