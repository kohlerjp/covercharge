from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
 	url(r'^$',views.index,name='index'),
 	url(r'^(?P<post_id>\d+)/$',views.detail,name='detail'),
 	url(r'^page(?P<page>\d+)/$',views.index_page,name='index_page'),
 	url(r'^(?P<post_id>\d+)/upvote/$',views.upvote,name='upvote'),
 	url(r'^(?P<post_id>\d+)/downvote/$',views.downvote,name='downvote'),
 	)