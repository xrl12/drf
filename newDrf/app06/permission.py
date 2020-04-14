from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_jwt.authentication import jwt_decode_handler

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # 用户对这个视图有没有 GET POST PUT PATCH DELETE 权限的分别判断
        if not request.user:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        """
        是用户过了has_permission 判断有权限以后，
        再判断这个用户有没有对一个具体的对象有没有操作权限。
        SAFE_METHODS : ('GET', 'HEAD', 'OPTIONS')
        """
        if not request.method in SAFE_METHODS:
            return request.user == obj.user
        return True



class MyAuthentication(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.META.get('HTTP_AUTHORIZATION')[5:]
        user = jwt_decode_handler(token)
        if user:
            return user.id == obj.user.id
        return False
