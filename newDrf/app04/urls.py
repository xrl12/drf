from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserDetail,UserList

router = DefaultRouter()
# router.register(r'articles',ArticleList.as_view(),base_name='article-list')
# router.register(r'groups',/GroupViewset)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
    path('', include(router.urls)),
]
