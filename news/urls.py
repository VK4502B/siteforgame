from django.conf.urls import url
from news.views import ArticleListView
from news.views import article_create
from . import views


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^create/$', article_create, name='create'),
]