# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,related_name="blogs")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ("-publish",)
    def __str__(self):
        return self.title
