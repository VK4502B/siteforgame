from django.db import models
from datetime import datetime
from django.utils.text import slugify
from unidecode import unidecode
from django.core.urlresolvers import reverse



class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    headline = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(blank=True, null=True,
        height_field='height_field',
        width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)
    pub_date = models.DateField('date published', default=datetime.now)
    pub_time = models.TimeField('time published', default=datetime.now)

    class Meta():
        ordering = ['-pub_date', '-pub_time']

    def __str__(self):
        return self.headline

    #def _get_unique_slug(self):
    #    slug = slugify(self.title)
    #    unique_slug = slug
    #    num = 1
    #    while Article.objects.filter(slug=unique_slug).exists():
    #        unique_slug = '{}-{}'.format(slug, num)
    #        num += 1
    #    return unique_slug


    def save(self):
        self.slug = slugify(unidecode(self.headline))
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('news:article_detail', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.headline