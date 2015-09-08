from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^snippets/', include('cyoa.urls', namespace="snippets")),
    url(r'^admin/', include(admin.site.urls)),
)