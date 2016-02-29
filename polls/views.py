
"""
This module implements the view of the polls application.
"""
from datetime import datetime

from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import Question, Choice
from .forms import QuestionChoiceFormset, QuestionForm


class AuthMixin(object):

    def get_context_data(self, **kwargs):
        context = super(AuthMixin, self).get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context


class IndexView(AuthMixin, generic.ListView):
    template_name = 'polls/index.djhtml'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.annotate(num_choices=Count('choice'))   \
            .filter(num_choices__gt=0).filter(pub_date__lte=timezone.now()).\
            order_by('-pub_date')[:5]


class DetailsView(AuthMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.djhtml'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(AuthMixin, generic.DetailView):
    model = Question
    template_name = 'polls/results.djhtml'

    def get_queryset(self):
        return Question.objects.annotate(
            num_answers=Count('choice')).filter(num_answers__gt=0)


class LoginTemplateView(AuthMixin, generic.TemplateView):
    pass


def logout(request, *args, **kwargs):

    extra_context = {'form': AuthenticationForm()}
    response = auth.views.logout(request,
                                 template_name='registration/logout.djhtml',
                                 extra_context=extra_context, *args, **kwargs)
    return response


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


def test(request):
    print 'bla'
    return render(request, 'polls/test.djhtml', {})


def login(request, *args, **kwargs):

    template_response = auth.views.login(request,  *args, **kwargs)

    # if isinstance(template_response, HttpResponseRedirect):
    #     return HttpResponseRedirect(kwargs['next'])
    # else:
    #     return template_response

    return template_response


# class QuestionSubmit(generic.CreateView):
#     model = Question

#     fields = ['question_text']

# @login_required
def addQuestion(request):

    if request.method == "GET":
        question = Question()
        formset = QuestionChoiceFormset(instance=question)
        return render(request, "polls/submit_question.djhtml",
                          context={"formset":formset,
                                       'form':QuestionForm(instance=question)})
    elif request.method == 'POST':
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            question.pub_date = datetime.now()
            question.submitter = request.user
            question.save()

            formset = QuestionChoiceFormset(request.POST, request.FILES)
            if formset.is_valid():
                for form in formset:
                    choice = form.save(commit=False)
                    choice.question = question
                    choice.save()

        return HttpResponseRedirect(reverse('polls:index'))

# @login_required
# def submit_question(request, *args, **kwargs):

#     pass
