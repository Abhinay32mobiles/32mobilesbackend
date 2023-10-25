from requests import Response
from rest_framework import generics , viewsets , filters, response , status, views
from django.db.models import Q

from .models import TV, Article, Statics, TagsArticle, Brand, Category, Mobile,TagsModel, ModelDetails, TagsArticle, TagsModel, YouTubeVideoDetails
from .serializers import ArticleSerializer, ArticleTagsSerializer, BrandSerializer, CategorySerializer, MobileSerializer, ModelDetailTagsSerializer, ModelDetailsSerializer, StaticsSerializer, TVSerializer, YouTubeVideoSerializer

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
    queryset = YouTubeVideoDetails.objects.all()
    serializer_class = YouTubeVideoSerializer

# Retrieve, update, or delete a specific YouTube video
class YouTubeVideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YouTubeVideoDetails.objects.all()
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
class ModelDetailsByCategoryView(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')  # Get the category_id from query parameters
        query = self.request.query_params.get('model_name', '')  # Get the model_name from query parameters

        if not category_id:
            # Handle the case where category_id is missing
            return ModelDetails.objects.none()

        # Filter by category_id and optional model_name
        queryset = ModelDetails.objects.filter(category_id=category_id)

        if query:
            queryset = queryset.filter(Q(model_name__icontains=query))  # Case-insensitive partial match

        return queryset
class CreateStaticsView(generics.CreateAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer
class ListStaticsView(generics.ListAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer
class UpdateStaticsView(generics.UpdateAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer
class PartialUpdateStaticsView(generics.UpdateAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        # Define the fields to update (replace with your actual field names)
        fields_to_update = [
            'homepage_cdn_links',
            'homepage_redirect_links',
            'homepage_banner_text',
            'homepage_button_text',
            'homepagevert_cdn_links',
            'homepagevert_redirect_links',
            'homepagevert_banner_text',
            'homepagevert_button_text',
            'homepagehori_cdn_links',
            'homepagehori_redirect_links',
            'homepagehori_banner_text',
            'homepagehori_button_text',
            'homepage_brand_banner_cdn',
            'articles_cdn_links',
            'articles_redirect_links',
            'articles_banner_text',
            'articles_button_text',
            'artilcevert_cdn_links',
            'artilcevert_redirect_links',
            'artilcevert_banner_text',
            'artilcevert_button_text',
            'artilcehori_cdn_links',
            'artilcehori_redirect_links',
            'artilcehori_banner_text',
            'artilcehori_button_text',
            'products_cdn_links',
            'products_redirect_links',
            'products_banner_text',
            'products_button_text',
            'productvert_cdn_links',
            'productvert_redirect_links',
            'productvert_banner_text',
            'productvert_button_text',
            'producthori_cdn_links',
            'producthori_redirect_links',
            'producthori_banner_text',
            'producthori_button_text',
            'product_priceband_array',
        ]
        
        # Merge the existing arrays with the new data for each field
        for field_name in fields_to_update:
            existing_data = getattr(instance, field_name)
            new_data = serializer.validated_data.get(field_name, [])
            updated_data = existing_data + new_data
            setattr(instance, field_name, updated_data)
        
        instance.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
class RetrieveStaticsView(generics.RetrieveAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer
class DeleteStaticsView(generics.DestroyAPIView):
    queryset = Statics.objects.all()
    serializer_class = StaticsSerializer
class ArticlesByTagView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']  # Get the tag ID from the URL parameter
        return Article.objects.filter(tags__id=tag_id)
class YouTubeVideoListByModelid(generics.ListAPIView):
    serializer_class = YouTubeVideoSerializer

    def get_queryset(self):
        model_id = self.kwargs['model_id']
        return YouTubeVideoDetails.objects.filter(model_details__model_id=model_id)
class ModelsByTagView(generics.ListAPIView):
    serializer_class = ModelDetailsSerializer

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']  # Get the tag name from the URL parameter
        return ModelDetails.objects.filter(tags__id=tag_id)
    