from django.contrib import admin
from django.urls import path, include

from .views import GameDetail, GameList

urlpatterns = [
    path('games/', GameList.as_view(), name='name-list'),
    path('games/<int:id>/', GameDetail.as_view(), name='name-detail')

]
