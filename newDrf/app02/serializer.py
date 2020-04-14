from rest_framework import serializers
serializers.ModelSerializer
from .models import Article
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=10)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    nvum = serializers.IntegerField(default=0)
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get("content",instance.content)
        instance.nvum = validated_data.get('nvum',instance.nvum)
        instance.save()
        return instance