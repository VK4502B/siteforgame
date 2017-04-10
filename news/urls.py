from django.conf.urls import url
from news.views import ArticleListView
from news.views import article_create
from news.views import ArticleDetailView
from . import views


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^create/$', article_create, name='create'),
]