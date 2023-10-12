from django.urls import path
from .views import ArticleDetailView, ArticleListCreateView, BrandListCreateView, BrandDetailView, CategoryDetailView, CategoryListCreateView, MobileDetailView, MobileListCreateView, ModelDetailsByBrandView, ModelDetailsByCategoryIdView, ModelDetailsDetailView, ModelDetailsListCreateView, ModelDetailsViewSet, TVDetailView, TVListCreateView, YouTubeVideoDetailView, YouTubeVideoListCreateView

app_name = 'appv1'

urlpatterns = [
    path('brands/', BrandListCreateView.as_view(), name='brand-list'),
    path('brands/<uuid:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('mobiles/', MobileListCreateView.as_view(), name='mobile-list'),
    path('mobiles/<uuid:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
    path('tvs/', TVListCreateView.as_view(), name='tv-list'),
    path('tvs/<uuid:pk>/', TVDetailView.as_view(), name='tv-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('modeldetails/', ModelDetailsListCreateView.as_view(), name='modeldetails-list'),
    path('modeldetails/<uuid:pk>/', ModelDetailsDetailView.as_view(), name='modeldetails-detail'),
    path('modeldetails/by_brand/<uuid:brand_id>/', ModelDetailsByBrandView.as_view(), name='modeldetails-by-brand'),
     path('modeldetails/by_category_id/<uuid:category_id>/', ModelDetailsByCategoryIdView.as_view(), name='modeldetails-by-category-id'),
     path('modeldetails2/', ModelDetailsViewSet.as_view(), name='modeldetails-list'),
      path('youtube-videos/', YouTubeVideoListCreateView.as_view(), name='youtube-video-list'),
    path('youtube-videos/<uuid:pk>/', YouTubeVideoDetailView.as_view(), name='youtube-video-detail'),
     path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<uuid:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    
    # Add more views and URL patterns for other models here
]
