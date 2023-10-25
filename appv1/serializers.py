from rest_framework import serializers
from .models import TV, Article, Brand, Category, Mobile, ModelDetails, Statics, TagsArticle, TagsModel, YouTubeVideoDetails

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ModelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelDetails
        fields = '__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideoDetails
        fields = '__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class ModelDetailTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = '__all__'

class ArticleTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsArticle
        fields = '__all__'
class StaticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statics
        fields = '__all__'
