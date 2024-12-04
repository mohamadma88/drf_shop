from django.urls import path
from .views import ArticleList, AddArticle, ArticleDetail

urlpatterns = [
    path('list', ArticleList.as_view(), name='list'),
    path('add', AddArticle.as_view(), name='add'),
    path('detail/<slug:slug>', ArticleDetail.as_view(), name='detail'),
]
