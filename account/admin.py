# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user","birth","phone")
    list_filter = ("phone",)

admin.site.register(UserProfile,UserAdmin)
