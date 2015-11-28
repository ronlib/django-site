
"""
This module implements the view of the polls application.
"""
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.djhtml'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.annotate(num_choices=Count('choice'))   \
            .filter(num_choices__gt=0).filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['auth_form'] = AuthenticationForm()
        return context


class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.djhtml'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.djhtml'

    def get_queryset(self):
        return Question.objects.annotate(num_answers=Count('choice')).filter(num_answers__gt=0)


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        # Redisplay the form
        return render(request, 'polls/detail.djhtml', {
            'question': p, 'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def get_user(request):
    # if request.method == 'POST':
    #     form = User.
    pass

def test(request):
    print 'bla'
    return render(request, 'polls/test.djhtml', {})
