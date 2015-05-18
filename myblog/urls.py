from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blog.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'^test/$', 'blog.views.test'),
    url(r'^archives/$', 'blog.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'blog.views.about_me', name = 'about_me'),
    url(r'^search/$','blog.views.blog_search', name = 'search'),
    )