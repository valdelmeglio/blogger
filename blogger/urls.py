from django.conf.urls import patterns, include, url
from blogger import views as blogger_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^admin/', include(admin.site.urls)),
   (r'^$', 'blogger.blog.views.index'),
url(r'^blog/view/(?P<slug>[^\.]+).html', 'blogger.blog.views.view_post', name='view_blog_post'),
url(r'^blog/category/(?P<slug>[^\.]+).html', 'blogger.blog.views.view_category', name='view_blog_category'),
url(r'^blog/postForm.html', 'blogger.blog.views.view_form', name='view_blog_form'),    

)