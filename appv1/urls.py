from django.urls import path
from .views import ArticleDetailView, ArticleListCreateView, ArticleSearchView, ArticleTagsDetail, ArticleTagsListCreateView, ArticleViewSet, ArticlesByTagView, BrandListCreateView, BrandDetailView, CategoryDetailView, CategoryListCreateView, ContactDetailPrimaryKeyOperationView, ContactMessageListCreateView, CreateStaticsView, DeleteStaticsView, ListStaticsView, MobileDetailView, MobileListCreateView, ModelDetailTagsListCreateView, ModelDetailsByBrandView, ModelDetailsByCategoryIdView, ModelDetailsByCategoryView, ModelDetailsDetailView, ModelDetailsListCreateView, ModelDetailsListbypriceandidsOpt, ModelDetailsSearchView, ModelDetailsViewSet, ModelTagsDetail, ModelsByTagView, PartialUpdateStaticsView, PriceStaticsListCreateView, PriceStaticsRetrieveUpdateDestroyView, RetrieveStaticsView, TVDetailView, TVListCreateView, UpdateStaticsView, YouTubeVideoDetailView, YouTubeVideoListByModelid, YouTubeVideoListCreateView

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
     path('modeldetailscustom/', ModelDetailsViewSet.as_view(), name='modeldetails-list'),
      path('youtube-videos/', YouTubeVideoListCreateView.as_view(), name='youtube-video-list'),
    path('youtube-videos/<uuid:pk>/', YouTubeVideoDetailView.as_view(), name='youtube-video-detail'),
     path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<uuid:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articlescustom/', ArticleViewSet.as_view(), name='article-list'),
    path('model-details-price-optID/', ModelDetailsListbypriceandidsOpt.as_view(), name='model-details-list'),
     path('article-tags/', ArticleTagsListCreateView.as_view(), name='article-tags'),
    path('model-detail-tags/', ModelDetailTagsListCreateView.as_view(), name='model-detail-tags'),
    path('modeltags/<int:pk>/', ModelTagsDetail.as_view(), name='modeltags-detail'),
    path('articletags/<int:pk>/', ArticleTagsDetail.as_view(), name='articletags-detail'),
    path('search/articlebytitle/', ArticleSearchView.as_view(), name='article-search'),
    path('search/productbyname/', ModelDetailsSearchView.as_view(), name='modeldetails-search'),
    path('modeldetails/by_category/', ModelDetailsByCategoryView.as_view(), name='modeldetails-by-category'),
    # Add more views and URL patterns for other models here
    #static paths
    #  path('statics/create/', CreateStaticsView.as_view(), name='create-statics'),
    path('statics/list/', ListStaticsView.as_view(), name='list-statics'),
    path('statics/update/<int:pk>/', UpdateStaticsView.as_view(), name='update-statics'),
    path('statics/retrieve/<int:pk>/', RetrieveStaticsView.as_view(), name='retrieve-statics'),
    # path('statics/delete/<int:pk>/', DeleteStaticsView.as_view(), name='delete-statics'),
    #static paths
     path('statics/partial-update/<int:pk>/', PartialUpdateStaticsView.as_view(), name='partial-update-statics'),
    path('articles-by-tag/<int:tag_id>/', ArticlesByTagView.as_view(), name='articles-by-tag'),
    path('models-by-tag/<int:tag_id>/', ModelsByTagView.as_view(), name='models-by-tag'),
    path('youtubevideos/<uuid:model_id>/', YouTubeVideoListByModelid.as_view(), name='youtube-video-list'),
     path('contact-messages/', ContactMessageListCreateView.as_view(), name='contact-message-list-create'),
    path('contact-messages/<int:pk>/', ContactDetailPrimaryKeyOperationView.as_view(), name='contact-message-detail'),
    path('price-statics/', PriceStaticsListCreateView.as_view(), name='price-statics-list-create'),
    path('price-statics/<uuid:pk>/', PriceStaticsRetrieveUpdateDestroyView.as_view(), name='price-statics-retrieve-update-destroy'),
]  
