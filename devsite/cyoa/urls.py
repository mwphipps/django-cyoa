from django.conf.urls import patterns, url

from cyoa import views

urlpatterns = patterns('',
 #   url(r'^$', views.IndexView.as_view(), name='index'),
 	url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<snippet_id>\d+)/choose/$', views.choose, name='choose'),
)
