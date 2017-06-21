from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^$', views.info, name='info'),
     url(r'^requests$', views.requests, name='requests'),
     url(r'^check_requests$', views.check_requests, name='check_requests'),
     url(r'^edit_form/$', views.edit_form, name='edit_form'),

]