from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ArticleList, ArticleDetail

router = DefaultRouter()
# router.register(r'articles',ArticleList.as_view(),base_name='article-list')
# router.register(r'groups',/GroupViewset)

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path('articles/<int:id>',ArticleDetail, name='article-detail'),
    path('', include(router.urls))
]
