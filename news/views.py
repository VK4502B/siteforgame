from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
import logging

from news.models import Article
from .forms import ArticleForm


log = logging.getLogger(__name__)

class ArticleListView(ListView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "article_create.html", context)


def article_update(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, instance=instance)
    if form.is_valid():
        log.warn("Form valid")
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "headline": instance.headline,
        "instance": instance,
        "form": form,
    }
    return render(request, "article_update.html", context)    