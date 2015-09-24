from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"

class ArtistListView(ListView):
    model = coremodels.Artist
    template_name = 'artist/list.html'

class ArtistDetailView(DetailView):
    model = coremodels.Artist
    template_name = 'artist/detail.html'
    context_object_name = 'artist'