from django.conf.urls import url
from news.views import ArticleListView
from news.views import ArticleDetailView
from news.views import article_create
from news.views import article_update
from . import views


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^create/$', article_create, name='create'),
    url(r'^article/(?P<slug>[-\w]+)/edit$', article_update, name='update')
]