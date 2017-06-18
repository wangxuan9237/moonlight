# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)

class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

