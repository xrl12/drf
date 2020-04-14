from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Article
from .serializer import ArticleSerializer


# Create your views here.
#
# class ArticleViewSet(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        data = JSONRenderer().render(data)
        print(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(data, **kwargs)


class ArticleList(APIView):
    def get(self, request, *args, **kwargs):
        arts = Article.objects.all()
        ser = ArticleSerializer(instance=arts, many=True)
        return JSONResponse(data=ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        ser = ArticleSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JSONResponse(data=ser.data, status=status.HTTP_201_CREATED)
        else:
            return JSONResponse(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


class MyException(BaseException):
    def __init__(self, message):
        self.message = message
        # return self.message


@api_view(['PUT', 'DELETE', 'GET'])
def ArticleDetail(request, id):
    try:
        art = Article.objects.get(id=id)
    except Article.DoesNotExist:
        # raise JSONResponse(data=MyException('没有这个用户'),status = status.HTTP_400_BAD_REQUEST)
        return HttpResponse('没有这个用户',status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        ser = ArticleSerializer(art)
        return JSONResponse(data=ser.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = ArticleSerializer(instance=art, data=data)
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        art.delete()
        return JSONResponse(data='删除成功', status=status.HTTP_200_OK)
