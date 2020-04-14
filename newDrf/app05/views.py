from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game
from .serializer import GameSerializer
from .mypermission import IsOwnReadOnly

# Create your views here.

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReadOnly]


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
