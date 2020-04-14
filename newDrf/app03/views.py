from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404

from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializer import ArticleSerializer, CategorySerializer, TagSerializer
from .models import Article, Category, Tag


# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        data = renderers.JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'

        super().__init__(data, **kwargs)


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = ArticleSerializer(instance=arts, many=True, context={'request': request})
        return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        ser = ArticleSerializer(data=data, context={'request': request})
        print(ser)
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)


def article_detail(request, id):
    try:
        arts = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse('没有这个用户')
    if request.method == 'GET':
        ser = ArticleSerializer(instance=arts, context={'request': request})
        return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = parsers.JSONParser().parse(request)
        ser = ArticleSerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
        return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        print('你猜我到哪里')
        ser = CategorySerializer(instance=categorys, many=True, context={'request': request})
        print("猜对了吗")
        return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        ser = CategorySerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
        return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_object(self, id):
        try:
            cats = Category.objects.get(id=id)
            return cats
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, id):
        cats = self.get_object(id=id)
        ser = CategorySerializer(instance=cats, context={'request': request})
        if cats:
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse('没有这个分组', status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        cats = self.get_object(id=id)
        if not cats:
            return HttpResponse('没有这个分组')
        data = parsers.JSONParser().parse(request)
        print('我走的是put方法')
        ser = CategorySerializer(instance=cats, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
        return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        cats = self.get_object(id)
        if not cats:
            return HttpResponse('没有这个分组')
        cats.delete()
        print('我走的是delete方法')
        return HttpResponse('删除成功', status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        ser = TagSerializer(instance=tags,many=True)
        return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        ser = TagSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_201_CREATED)
        return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(APIView):
    def get_object(self, id):
        try:
            tags = Tag.objects.get(id=id)
            return tags
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request):
        tag = self.get_object(id=request._request.id)
        ser = TagSerializer(instance=tag)
        return JSONResponse(ser.data, status=status.HTTP_200_OK)

    def put(self, request):
        tag = self.get_object(id=request._request.id)
        data = parsers.JSONParser().parse(request_request)
        ser = TagSerializer(instance=tag, data=data)
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_200_OK)
        return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        tag = self.get_object(id=request._request.id)
        tag.delete()
        return HttpResponse('删除成功',status = status.HTTP_200_OK)

# class CategoryViewset(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class ArticleViewset(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
