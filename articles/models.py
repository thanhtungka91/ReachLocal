# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Source(models.Model): 
    source_id = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    author = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    urlToImage = models.CharField(max_length=200)
    publishedAt = models.DateTimeField('date published')
