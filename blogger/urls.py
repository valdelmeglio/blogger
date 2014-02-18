from django.conf.urls import patterns, include, url
from blogger import views as blogger_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^admin/', include(admin.site.urls)),
   (r'^$', 'blogger.blog.views.index'),
   (r'^login', 'django.contrib.auth.views.login'),
url(r'^view_form', 'blogger.blog.views.view_form', name='view_form'),    
url(r'^(?P<id>[^\.]+)/edit.html', 'blogger.blog.views.edit_post', name='view_edit_post'),
url(r'^(?P<id>[^\.]+).html', 'blogger.blog.views.view_post', name='view_blog_post'),
url(r'^(?P<slug>[^\.]+).html', 'blogger.blog.views.view_category', name='view_blog_category'),

)
