# 这个项目还未完成，将来会显示的内容请参考设计稿：
手机小程序设计稿：https://www.figma.com/design/OudupNW0gaAaclXLltVWqF/logoflowerfrontend?node-id=0-1&t=TnkNiTQLW1UOTIEr-1
ToB端管理后台设计稿：[[https://www.figma.com/proto/fDorE7AEPpwA1FCiYKr1FK/flowerbackend?node-id=0-1&t=94Bj2nTEpSsiUHnG-1](https://www.figma.com/design/fDorE7AEPpwA1FCiYKr1FK/flowerbackend?node-id=0-1&t=94Bj2nTEpSsiUHnG-1)](https://www.figma.com/design/fDorE7AEPpwA1FCiYKr1FK/flowerbackend?node-id=0-1&t=ZhhM4uEAQYUpQKJJ-1)

# Retail Flower Shop System

基于 uni-app、Vue 3、TypeScript、Django REST Framework 和 MySQL 开发的零售花店系统，包含兼容 H5 与微信小程序的商城、管理后台、后端 API 和部署配置。

- H5 商城：[http://115.29.203.212/retail-flower/#/](http://115.29.203.212/retail-flower/#/)
- 管理后台：[http://115.29.203.212/retail-flower-admin/](http://115.29.203.212/retail-flower-admin/)
- 管理后台演示账号：`admin`
- 管理后台演示密码：`12345678`

## 技术栈

- 商城：uni-app / Vue 3 / TypeScript / Vite
- 管理后台：Vue 3 / TypeScript / Element Plus / Pinia / Axios / Vite
- 后端：Python / Django / Django REST Framework / MySQL
- 图片存储：阿里云 OSS
- 部署：Nginx / Gunicorn / systemd

## 项目亮点

- 使用同一套 uni-app 商城代码兼容 H5 和微信小程序。
- 商品根据上架状态与分类动态筛选，并按照发布时间在双列列表中排列。
- 管理后台使用 Session 与 CSRF 完成员工登录和访问控制。
- 实现商品主图、详情图上传和商品发布流程，图片由阿里云 OSS 存储并通过签名地址访问。
- 前台商城、管理后台、后端 API 与部署配置分目录维护。

## 目录结构

```text
retail-flower-shop-system
├── admin-frontend/   Vue 3 管理后台
├── client-frontend/  uni-app H5 与微信小程序商城
├── deployment/       Nginx 与 systemd 部署配置
└── server-backend/   Django REST Framework 后端
```

## 本地运行

### 1. 启动后端

准备 Python 3、MySQL 和阿里云 OSS 配置，然后执行：

```bash
cd server-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

启动前需要根据本地环境填写 `server-backend/.env` 中的数据库和 OSS 配置。

### 2. 启动管理后台

```bash
cd admin-frontend
cp .env.example .env.development
npm install
npm run dev
```

### 3. 启动 H5 商城

```bash
cd client-frontend
cp .env.example .env.development
npm install
npm run dev:h5
```

### 4. 启动微信小程序

```bash
cd client-frontend
npm run dev:mp-weixin
```

编译后，在微信开发者工具中导入 `client-frontend/dist/dev/mp-weixin`。

## 环境变量说明

仓库只保留 `.env.example`。真实的数据库密码、Django 密钥和 OSS 凭据不会提交到 Git。

- `admin-frontend/.env.example`：管理后台 API 路径
- `client-frontend/.env.example`：商城 API 地址和路径
- `server-backend/.env.example`：Django、MySQL 与 OSS 配置

## 数据说明

数据库结构通过 Django migrations 管理，公开仓库不包含本地数据库文件和运行时业务数据。

# 图片
![Uploading image.png…]()

<img width="992" height="665" alt="image" src="https://github.com/user-attachments/assets/4e988ec5-de88-4962-a414-8af84ee72695" />

<img width="508" height="1020" alt="image" src="https://github.com/user-attachments/assets/7610f6c7-7c0b-475c-9762-52ac8f3e7f85" />

<img width="351" height="671" alt="image" src="https://github.com/user-attachments/assets/7ad344b9-a11e-4b62-a50c-dce6d7d6d097" />

<img width="850" height="594" alt="image" src="https://github.com/user-attachments/assets/b780781d-6122-47b5-9301-b81c8fb4f39a" />


<img width="864" height="570" alt="image" src="https://github.com/user-attachments/assets/1789eaa5-be63-407c-bee2-dab3280b0bed" />

<img width="461" height="502" alt="image" src="https://github.com/user-attachments/assets/b58f28a5-9f00-4c5e-9a1d-32a946409c30" />

<img width="1015" height="722" alt="image" src="https://github.com/user-attachments/assets/5f7276ae-9b14-40a2-bb66-8d34099bb22e" />

