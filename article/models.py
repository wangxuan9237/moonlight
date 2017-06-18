# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from slugify import slugify
# Create your models here.
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name="article_column")
    column = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

class ArticlePost(models.Model):
    author = models.ForeignKey(User,related_name="article",blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(max_length=500,blank=True,null=True)
    column = models.ForeignKey(ArticleColumn,related_name="article_column",blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    created = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)
    class Meta:
        ordering = ("-created",)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])
