
from .views import ArticleListView, ArticleUpdateView,  ArticleDetailView, ArticleDeleteView,ArticleCreateView ,ArticleViewSet, ArticleCreateREST
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'json_articles', ArticleViewSet, basename='art')

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_add'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest_article/', ArticleCreateREST.as_view()),
]
