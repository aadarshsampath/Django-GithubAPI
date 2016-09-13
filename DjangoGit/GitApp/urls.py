from django.conf.urls import url

from GitApp import views

urlpatterns = [ 
	url(r'^profile/$', views.profile, name='profile'),
]