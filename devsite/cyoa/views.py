from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


from cyoa.models import Choice, Snippet, Story

# The index view is only loaded once
def index(request):
    story_list = Story.objects.all
    context = {'story_list': story_list}
    return render(request, 'cyoa/index.html', context)

# The detail view is loaded every time a choice is made.    
class DetailView(generic.DetailView):
    model = Snippet
    template_name = 'cyoa/detail.html'

# Results will be expanded to show player choice results in the end. For now, use stories/1/results/ to test
class ResultsView(generic.DetailView):
    model = Snippet
    template_name = 'cyoa/results1.html'

# Here the actual "choice" (vote) is cast and lastly we are sent to the story snippet detail based on the snippet_link from the choice.
def choose(request, snippet_id):
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

