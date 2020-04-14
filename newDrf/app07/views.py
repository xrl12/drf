from django.shortcuts import render

from rest_framework import generics

from .custom_json_response import JSONResponse
from .models import Game
from .serializer import GameSerializer
from .custom_model_view_set import ListModelMixin
from .custom_page_number import MyPageNumberPagination

# Create your views here.
class GameList(ListModelMixin):
    throttle_classes = []
    # queryset = Game.objects.all()
    lookup_field = 'id'
    serializer_class = GameSerializer

    def get_queryset(self):
        order = self.request.query_params.get('ordering')
        if not order:
            queryset = Game.objects.filter(status=1).all()
        else:
            queryset = Game.objects.order_by(order)
        if self.request.version == 'v1':
            queryset = Game.objects.filter(status=1).all()
            return queryset
        else:
            queryset = Game.objects.filter(status == 0).all()
            return queryset


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.version == 'v1':
            queryset = Game.objects.filter(status=1).all()
        else:
            queryset = Game.objects.filter(status == 0).all()
