from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'artist/$', coreviews.ArtistListView.as_view()),
 url(r'artist/(?P<pk>\d+)/detail/$', coreviews.ArtistDetailView.as_view(), name ='artist_list'),
 url(r'artist/create/$', coreviews.ArtistCreateView.as_view()),
 url(r'search/$', coreviews.SearchListView.as_view()),
 url(r'artist/(?P<pk>\d+)/update/$', coreviews.ArtistUpdateView.as_view(), name='artist_update'),
 url(r'artist/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='review_create'),
 url(r'artist/(?P<pk>\d+)/review/update/$', coreviews.ReviewUpdateView.as_view(), name='review_update'),
 url(r'entrance/$', coreviews.entrance),
 url(r'^accounts/login/$',  login),
 url(r'^accounts/logout/$', logout, {'template_name': 'base/index.html', 'next_page': '/'}, name='sign-out'),
 )
