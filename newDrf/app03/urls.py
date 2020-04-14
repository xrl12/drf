from django.contrib import admin
from django.urls import path, include

# from rest_framework.routers import DefaultRouter   #从rest_framework.routers导入DefaultRouter

from .views import category_list,CategoryDetail,article_list,article_detail,tag_list,TagDetail
# from .views import ArticleViewset,CategoryViewset

# router = DefaultRouter()  #创建一个DefaultRouter对象
# router.register(r'articles',ArticleViewset)
# router.register(r'categorys',CategoryViewset)  # 把自己的路由注册进去，第一个传入路径，第二个传入类视图


urlpatterns = [
    # path('', include(router.urls)),
    # path('categorys/<int:pk>/', CategoryViewset.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': "destroy"
    # }), name='categorys-detail'),
    # path('articles/<int:pk>/', ArticleViewset.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': "destroy"
    # }), name='articles_detail'),
    # path('categorys-detail/<int:id>',CategoryViewset.as_view()),
    path('categorys-list/', category_list),
    path('categorys-detail/<int:id>/', CategoryDetail.as_view(), name='categorys_detail'),
    path('articles-list/', article_list),
    path('articles-detail/<int:id>/', article_detail, name='articles_detail'),
    path('tags-list/',tag_list),
    path('tags-detail/<int:id>/',TagDetail.as_view),
    # 由于rest_framework里面默认id为pk所有我们这里需要把id改为pk
    # path('',include(router.urls)),  #  把告诉django要是有这个视图的话，就去router.urls
    # path("categorys/",CategoryViewset.as_view(),)

]
