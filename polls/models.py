import datetime
from django.contrib import auth
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    submitter = models.ForeignKey(auth.models.User, null=False,
                                default=auth.models.User.objects.get_or_create(
                                      username="unknown")[0].pk,
                                  on_delete=models.SET(
                                      auth.models.User.objects.get_or_create(
                                          username="deleted")[0].pk))

    # submitter = models.ForeignKey(auth.models.User, null=False,
    #                                   default=1,
    #                                   on_delete=models.SET(2))

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
