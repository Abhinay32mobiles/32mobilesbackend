from rest_framework import generics , viewsets , filters, response , status, views
from django.db.models import Q
from .models import TV, Article, TagsArticle, Brand, Category, Mobile,TagsModel, ModelDetails, TagsArticle, TagsModel, YouTubeVideo
from .serializers import ArticleSerializer, ArticleTagsSerializer, BrandSerializer, CategorySerializer, MobileSerializer, ModelDetailTagsSerializer, ModelDetailsSerializer, TVSerializer, YouTubeVideoSerializer

class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
class MobileListCreateView(generics.ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
class TVListCreateView(generics.ListCreateAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer

class TVDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ModelDetailsListCreateView(generics.ListCreateAPIView):
    queryset = ModelDetails.objects.all()
    serializer_class = ModelDetailsSerializer

class ModelDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelDetails.objects.all()
    serializer_class = ModelDetailsSerializer
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelDetailsByBrandView(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        brand_id = self.kwargs['brand_id']
        return ModelDetails.objects.filter(brand_id=brand_id)
class ModelDetailsByCategoryIdView(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']  # Get the category_id from the URL parameter
        return ModelDetails.objects.filter(category__category_id=category_id)
class ModelDetailsViewSet(views.APIView):
     def get(self, request, format=None):
        queryset = ModelDetails.objects.all()

        category_id = request.query_params.get('category_id')
        model_details_id = request.query_params.get('modelDetails_id')
        brand_id = request.query_params.get('brand_id')

        if category_id:
            queryset = queryset.filter(category=category_id)

        if model_details_id:
            queryset = queryset.filter(model_id=model_details_id)

        if brand_id:
            queryset = queryset.filter(brand=brand_id)

        serializer = ModelDetailsSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
class YouTubeVideoListCreateView(generics.ListCreateAPIView):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer

# Retrieve, update, or delete a specific YouTube video
class YouTubeVideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleViewSet(views.APIView):
    def get(self, request, format=None):
        queryset = Article.objects.all()

        category_id = request.query_params.get('category_id')
        model_details_id = request.query_params.get('modelDetails_id')
        brand_id = request.query_params.get('brand_id')

        if category_id:
            queryset = queryset.filter(category=category_id)

        if model_details_id:
            queryset = queryset.filter(products=model_details_id)

        if brand_id:
            queryset = queryset.filter(brands=brand_id)

        serializer = ArticleSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
class ModelDetailsListbypriceandidsOpt(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        # Get the price range parameters from the request
        lower_price = self.request.query_params.get('lower_price')
        higher_price = self.request.query_params.get('higher_price')

        # Start with all ModelDetails objects
        queryset = ModelDetails.objects.all()

        # Filter by price range if provided
        if lower_price is not None:
            queryset = queryset.filter(price__gte=lower_price)
        if higher_price is not None:
            queryset = queryset.filter(price__lte=higher_price)

        # Get optional category_id and brand_id parameters
        category_id = self.request.query_params.get('category_id')
        brand_id = self.request.query_params.get('brand_id')
        model_details_id = self.request.query_params.get('modelDetails_id')

        # Filter by category_id if provided
        if category_id is not None:
            queryset = queryset.filter(category__category_id=category_id)

        # Filter by brand_id if provided
        if brand_id is not None:
            queryset = queryset.filter(brand__brand_id=brand_id)
        if model_details_id:
            queryset = queryset.filter(model_id=model_details_id)

        return queryset
class ArticleTagsListCreateView(generics.ListCreateAPIView):
    queryset = TagsArticle.objects.all()
    serializer_class = ArticleTagsSerializer

class ModelDetailTagsListCreateView(generics.ListCreateAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = ModelDetailTagsSerializer
class ModelTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = ModelDetailTagsSerializer

class ArticleTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagsArticle.objects.all()
    serializer_class = ArticleTagsSerializer

class ArticleSearchView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        queryset = Article.objects.filter(Q(title__icontains=query))
        return queryset
class ModelDetailsSearchView(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        queryset = ModelDetails.objects.filter(Q(model_name__icontains=query))
        return queryset