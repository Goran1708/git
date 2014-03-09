from django.conf.urls import patterns, include, url
from news import views

urlpatterns = patterns('',
    # ...
    (r'^search/$', views.search),
    (r'^$', views.home),
    # ...
)