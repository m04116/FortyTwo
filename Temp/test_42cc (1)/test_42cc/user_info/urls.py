from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^$', views.info, name='info'),
     url(r'^requests', views.requests, name='requests'),

]