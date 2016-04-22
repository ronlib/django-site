from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', views.login,
        {'template_name': 'registration/login.djhtml'}, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^', include('django.contrib.auth.urls'),
        {'template_name': 'registration/login.djhtml'}),
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
        name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^about/$', views.LoginTemplateView.as_view(
        template_name='polls/about.djhtml'), name='about'),
    # url('^question', login_required(views.QuestionSubmit.as_view(
    #     template_name="polls/submit_question.djhtml")), name='add_question'),
    url('^question', login_required(views.addQuestion), name='add_question'),
    url('^graph/', TemplateView.as_view(template_name='polls/graph.djhtml')),
]
