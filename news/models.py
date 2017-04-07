from django.db import models
from datetime import datetime

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField('date published', default=datetime.now)


    def __str__(self):
        return self.headline

    def __unicode__(self):
        return self.headline