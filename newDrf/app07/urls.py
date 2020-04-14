from django.urls import path,include

from .views import GameList,GameDetail

urlpatterns = [
    path('games/',GameList.as_view(),name='game-list'),
    path('games/<int:id>/',GameDetail.as_view(),name='game-detail')
]
