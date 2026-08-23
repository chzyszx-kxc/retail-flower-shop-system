# Django 依赖
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 员工姓名是业务信息；username 是员工的登录账号。
    employee_name = models.CharField(max_length=100)

    # 预留的职位信息，仅用于展示；V1 不直接使用它判断权限。
    job_title = models.CharField(max_length=100, blank=True)
