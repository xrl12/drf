from rest_framework import serializers

from .models import Category, Article, Tag


# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#
#         model = Article
#
#
#
# class CategorySerializer(serializers.Serializer):
#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     name = serializers.CharField(required=True, max_length=20)
#
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.save()
#         return instance


# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     class Meta:
#         model = Article
#         fields = "__all__"
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.StringRelatedField()
#     class Meta:
#         model = Category
#         fields = "__all__"

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Article
#         fields = "__all__"
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
#     class Meta:
#         model = Category
#         fields = "__all__"


# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = "__all__"
#         extra_kwargs = {
#             'url':{
#                 'view_name':"app03:articles_detail",
#                 'lookup_field':"id",
#             },
#             'category': {
#                 'view_name': 'app03:categorys_detail', 'lookup_field': 'id'
#             },
#         }
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id','name','articles')
#         extra_kwargs = {
#             'url':{
#                 'view_name':"app03:categorys_detail",
#                 #view_name 和 urls.py 中的 name 参数相对应，表示使用哪个 url
#                 # app03表示根基路由，categorys_detail表示应用级路由
#
#                 'lookup_field':'id',  #表示用哪个字段来作为 url 的唯一识别标记
#             },
#             'articles':{
#                 "view_name":"app03:articles_detail",
#                 'lookup_field':'id'
#             }
#         }

#
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.HyperlinkedRelatedField(
#         lookup_url_kwarg='id',
#         read_only=True,
#         lookup_field='id',
#         view_name='app03:categorys_detail'
#     )
#     class Meta:
#         model = Article
#         fields = "__all__"
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.HyperlinkedRelatedField(
#         many=True,
#         lookup_field='id',
#         lookup_url_kwarg='id',
#         view_name='app03:articles_detail',
#         read_only=True
#     )
#     class Meta:
#         model = Category
#         fields = '__all__'


# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     category = serializers.HyperlinkedIdentityField(
#         view_name='app03:categorys_detail',
#         lookup_field='id',
#     )
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {
#                 'view_name': 'app03:articles_detail',
#                 'lookup_field': 'id'
#             }
#         }
#
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     article = serializers.HyperlinkedIdentityField(
#         view_name='app03:articles_detail',
#         lookup_field='id',
#         # many=True,
#         lookup_url_kwarg='id',
#     )
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         extra_kwargs = {
#             'url':{
#                 'view_name':"app03:categorys_detail",
#                 'lookup_field':'id',
#             }
#         }


# class ArticleSerializer(serializers.ModelSerializer):
#     # category = serializers.StringRelatedField()
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#         extra_kwarg = {
#             'url': {
#                 'view_name': 'app03:articles-detail',
#                 'lookup_fild': 'id',
#             }
#         }
#     # def to_representation(self, instance):
#     #     representation = super(ArticleSerializer, self).to_representation(instance)
#     #     representation['category'] = CategorySerializer(instance.category).data
#     #     representation['title'] = TagSerializer(instance.tags, many=True).data
#     #     return representation
#     def create(self, validated_data,):
#
#         print(validated_data.get('category'))
#         return Article.objects.create(**validated_data)
#
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     article = serializers.StringRelatedField()
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         extra_kwarg = {
#             'url': {
#                 'view_name': 'app03:articles-detail',
#                 'lookup_field': 'id'
#             },
#             'article': {
#                 'view_name': 'app03:categorys-detail',
#                 'lookup_field': 'id',
#             }
#         }

#
# class ArticleSerializer(serializers.ModelSerializer):
#     # category = serializers.HyperlinkedRelatedField(
#     #     view_name='app03:categorys_detail',
#     #     lookup_field='id',
#     #     lookup_url_kwarg='id',
#     #     read_only=True
#     # )
#     # category = CategorySerializer()
#     class Meta:
#         model = Article
#         fields = '__all__'
#         depth = 3
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     # articles = serializers.HyperlinkedIdentityField(
#     #     view_name='app03:categorys_detail',
#     #     lookup_field='id',
#     #     lookup_url_kwarg='id',
#     #     many=True,
#     #     read_only=True
#     # )
#     articles = ArticleSerializer(many=True)
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         depth = 2
#


# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Article
#         fields = '__all__'
#         depth = 1
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = ArticleSerializer(many=True)
#     count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         depth = 2
#
#     def get_count(self, obj):
#
#         return obj.articles.count()

# class MyCharField(serializers.CharField):
#     def to_representation(self, value):
#         data_list = []
#         for val in value:
#             data_list.append(
#                 {
#                     'title': val.title,
#                     'content': val.content,
#                     'nvum': val.nvum
#                 }
#             )
#         return data_list
#
# class ArticleSerializer(serializers.ModelSerializer):
#     cate = serializers.CharField(source=('category.name'))
#
#     class Meta:
#         model = Article
#         fields = "__all__"
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     arts = MyCharField(source=('articles.all'))
#
#     class Meta:
#         model = Category
#         fields = ('id', 'arts', 'name', 'articles')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        depth = 2


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%m:%S')
    class Meta:
        model = Tag
        fields = '__all__'

        
