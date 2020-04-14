from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins, generics


from .serializer import UserSerializer
from .models import User

# Create your views here.

#
# @api_view(['GET', 'POST'])
# def user_list(request):
#     if request.method == 'GET':
#         user = User.objects.all()
#         ser = UserSerializer(instance=user, many=True)
#         return Response(data=ser.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         ser = UserSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(data=ser.data, status=status.HTTP_200_OK)
#         return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
#

# class UserDetail(APIView):
#     def get_object(self, id):
#         try:
#             users = User.objects.get(id=id)
#             return users
#         except User.DoesNotExist:
#             raise Http404
#
# def get(self, request, *args, **kwargs):
#     user = self.get_object(kwargs.get('id'))
#     ser = UserSerializer(instance=user)
#     return Response(data=ser.data, status=status.HTTP_200_OK)
#
# def put(self, request, *args, **kwargs):
#     user = self.get_object(kwargs.get('id'))
#     ser = UserSerializer(instance=user, data=request.data)
#     if ser.is_valid():
#         ser.save()
#         return Response(data=ser.data, status=status.HTTP_200_OK)
#
# def patch(self, request, *args, **kwargs):
#     user = self.get_object(kwargs.get('id'))
#     ser = UserSerializer(instance=user, data=request.data, partial=True)
#     if ser.is_valid():
#         ser.save()
#         return Response(data=ser.data, status=status.HTTP_200_OK)
#     return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
# def delete(self, *args, **kwargs):
#     user = self.get_object(kwargs.get("id"))
#     user.delete()
#     return Response(data='删除成功', status=status.HTTP_200_OK, )



"""
类视图
"""
# from rest_framework import mixins,generics
# class UserList(mixins.CreateModelMixin,  # 创建数据  post请求
#                    mixins.ListModelMixin,  # 获取数据  get请求
#                generics.GenericAPIView):  # 里面有几个共用类
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = id
#
#     def get(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# from rest_framework import mixins,generics
# class UserDetail(mixins.RetrieveModelMixin,  # 获取单个数据 get请求
#                  mixins.UpdateModelMixin,  # 跟新数据 patch请求
#                  mixins.DestroyModelMixin,  # 删除数据 delete请求
#                  generics.GenericAPIView):  # 公共类
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'  # GenericAPIView 获取对象时，rest framework默认是pk
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


'''
公共类试图
'''



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
