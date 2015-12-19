import datetime
from django.contrib import auth
from django.db import models
from django.utils import timezone


def get_sentinel_user(is_deleted=True):
    if is_deleted:
        username = 'deleted'
    else:
        username = 'unknown'
    return auth.get_user_model().objects.get_or_create(username=username)[0]


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # submitter = models.ForeignKey(auth.models.User, models.SET(
    #     get_sentinel_user(is_deleted=True)))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
