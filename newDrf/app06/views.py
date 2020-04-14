import time
import hashlib

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, SessionAuthentication, \
    TokenAuthentication
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.versioning import BaseVersioning
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import User, UserToken
from .permission import MyPermission, MyAuthentication
from .custom_json_response import JSONResponse

# Create your views here.
def get_md5(user):
    ctime = str(time.time())
    md5 = hashlib.md5(bytes(user, encoding='utf-8'))
    md5.update(bytes(ctime, encoding='utf-8'))
    return md5.hexdigest()


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {
            'code': 1,
            'msg': None,
            'data': {}
        }
        user = request._request.POST.get('username')
        password = request._request.POST.get('password')
        obj = User.objects.filter(name=user, pwd=password).first()
        if not obj:
            ret['msg'] = '账号或者密码错误'
            ret['code'] = 1
            return JsonResponse(ret)
        token = get_md5(user)
        UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        ret['token'] = token
        return JsonResponse(ret)


# class MyAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         token = request.META.get('HTTP_TOKEN')
#         print(token)
#         obj = UserToken.objects.filter(token=token).first()
#         if not obj:
#             raise exceptions.AuthenticationFailed('请检查你的token')
#         else:
#             return (obj.user, obj)  # 这里要传入一个元组


class Cars(APIView):
    """
    BasicAuthentication: 基于用户名密码
    SessionAuthentication：基于session
    TokenAuthentication：基于token
    """

    authentication_classes = [
        # MyAuthentication
        JSONWebTokenAuthentication
        # BasicAuthentication
    ]
    # 权限
    permission_classes = [
        # MyPermission

        MyAuthentication,
        IsAuthenticated,

    ]

    # throttle_classes = [
    #     'app06.mythrottle.UserThrottle'
    # ]

    def get(self, request, *args, **kwargs):
        ctx = {
            "code": 1,
            "msg": 'OK',
            "data": {
                'good': [
                    {
                        'name': "苹果",
                        'price': 12
                    },
                    {
                        'name': "香蕉",
                        'price': 13
                    }
                ]
            }
        }
        # JSONResponse是自己重写的
        return JSONResponse(ctx, code=200, msg="success", status=status.HTTP_200_OK)

class Service(APIView):
    # 通过request.version来获取版本号
    def get(self,request,*args,**kwargs):
        if request.version =='v1':
            ctx = {
                'code':1,
                'msg':'ok',
                'data':{}
            }
        else:
            ctx = {
                'code': 2,
                'msg': 'ok',
                'data': {}
            }

        return JSONResponse(ctx,code=200,)