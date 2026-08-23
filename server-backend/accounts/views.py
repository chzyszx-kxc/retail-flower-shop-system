# Django 依赖
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

# 第三方依赖
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

# 当前应用依赖
from accounts.serializers import CurrentUserSerializer, LoginSerializer


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """校验账号密码并创建登录 Session"""

    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )

        if user is None:
            return Response(
                {'detail': '账号或密码错误'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)

        return Response(CurrentUserSerializer(user).data)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class CsrfCookieView(APIView):
    """向浏览器写入 CSRF Cookie"""

    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserView(APIView):
    """返回当前 Session 对应的登录员工"""

    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(CurrentUserSerializer(request.user).data)


class LogoutView(APIView):
    """结束当前员工的登录 Session"""

    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)
