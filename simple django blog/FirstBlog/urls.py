from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'blog.views.home', name='home'),
	url(r'^admin/doc', include('django.contrib.admindocs.urls')), # enables admin documentation
	url(r'^admin/', include(admin.site.urls)),
)
