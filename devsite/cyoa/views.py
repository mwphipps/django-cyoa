from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


from cyoa.models import Choice, Snippet

# The index view is only loaded once
class IndexView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		template_name = 'cyoa/index.html'
		return render(request, 'cyoa/index.html', {
			# This title is only for the original index page
            'cyoatitle': "Kentucky Wanderer",
            'cyoaauthor': 'Michael Phipps Jr.',
            'cyoayear': '2014',
            'cyoadescript': "Frustrated with modern life, you decide to take a hike by yourself to get away from things.",
        })

# The detail view is loaded every time a choice is made.    
class DetailView(generic.DetailView):
    model = Snippet
    template_name = 'cyoa/detail.html'

# Results will be expanded to show player choice results in the end. For now, use stories/1/results/ to test
class ResultsView(generic.DetailView):
    model = Snippet
    template_name = 'cyoa/results1.html'

# Here the actual "choice" (vote) is cast and lastly we are sent to the story snippet detail based on the snippet_link from the choice.
def vote(request, snippet_id):
    p = get_object_or_404(Snippet, pk=snippet_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the story snippet form.
        return render(request, 'cyoa/detail.html', {
            'snippet': p,
            'error_message': "You didn't select a choice.",
        })
    else:
     #   selected_choice.votes += 1
     #   selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('snippets:detail', args=(selected_choice.snippet_link,)))   

