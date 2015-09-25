from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from sitegate.decorators import redirect_signedin, sitegate_view
from django.contrib import auth
from django.contrib.auth.views import login, logout
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

    def get_context_data(self, **kwargs):
		context = super(ArtistDetailView, self).get_context_data(**kwargs)
		artist = coremodels.Artist.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.Review.objects.filter(artist=artist, user=self.request.user)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews[0]
			else:
				context['user_review'] = None

		return context

class ArtistCreateView(CreateView):
	model = coremodels.Artist
	template_name = 'base/form.html'
	fields = "__all__"

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields =['description', 'rating']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.artist = coremodels.Artist.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.artist.get_absolute_url()

class ReviewUpdateView(UpdateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields =['description', 'rating']

	def get_object(self):
		return coremodels.Review.objects.get(artist__id=self.kwargs['pk'], user=self.request.user)

	def get_success_url(self):
		return self.object.artist.get_absolute_url()



class ArtistUpdateView(UpdateView):
	model = coremodels.Artist
	template_name = 'base/form.html'
	fields = "__all__"

class SearchListView(ArtistListView):

	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query', '')
		return coremodels.Artist.objects.filter(title__icontains=incoming_query_string)

@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.

def entrance(request):
	return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

def logout_view(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/user/loggedout/")
