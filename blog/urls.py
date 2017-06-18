from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$',views.blog_title,name='blog_title'),
        url(r'(?P<blog_id>\d)/$',views.blog_body,name='blog_body'),
        ]
