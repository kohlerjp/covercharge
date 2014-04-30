from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
 	url(r'^new/$',views.new,name='new'),
 	url(r'^create/$',views.create,name='create'),
 	url(r'^logout/$',views.logout_view,name='logout'),
 	url(r'^sign_in/$',views.login_view,name='login_view'),
 	url(r'^login/$',views.login_action,name='login_action'),
 	)