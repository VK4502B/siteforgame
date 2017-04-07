from django.conf.urls import url
from news.views import ArticleListView
from . import views

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
]