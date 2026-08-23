# 第三方依赖
from rest_framework import serializers

# 当前应用依赖
from accounts.models import User


class LoginSerializer(serializers.Serializer):
    """校验登录请求中的账号和密码格式"""

    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )


class CurrentUserSerializer(serializers.ModelSerializer):
    """将当前登录员工转换成前端需要的 JSON 数据"""

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'employee_name',
            'job_title',
        ]
