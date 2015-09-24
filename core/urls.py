from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'artist/$', coreviews.ArtistListView.as_view()),
 url(r'artist/(?P<pk>\d+)/detail/$', coreviews.ArtistDetailView.as_view(), name ='artist_list'),
)
