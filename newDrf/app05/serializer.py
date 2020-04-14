from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        lookup_url_kwarg='id',
        view_name="app05:name-detail"
    )

    class Meta:
        model = Game
        fields = "__all__"
