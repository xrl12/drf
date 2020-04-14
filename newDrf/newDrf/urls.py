"""newDrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from  rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from app01.views import StudentViewset,GroupViewset
# from app03.views import ArticleViewset,CategoryViewset
# from app03.views import ArticleViewset,CategoryViewset
router = DefaultRouter()
router.register(r'students',StudentViewset)
router.register(r'groups',GroupViewset)
# router.register(r'articles',ArticleViewset)
# router.register(r'categorys',CategoryViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include(("app02.urls","app02"))),
    # path('api/',include(('app03.urls','app03'),namespace='app03')),
    # path('',include(('app04.urls','app04'),namespace='app04')),
    # path("",include(("app05.urls","app05"),namespace="app05")),
    path('',include(('app06.urls','app06'),namespace='app06')),
    path('api/<str:version>/',include(('app07.urls','app07'))),
    # path('api/token/',views.ObtainAuthToken.as_view()),

    # path('api-token-auth/', obtain_jwt_token),  # 使用post方法 在请求体里面传入username和password
    path('docs/', include_docs_urls(title='测试平台接口文档')),
    path('',include(router.urls)),

]
