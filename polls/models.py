import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """this class create question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ended', null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """ return true if the question was published within recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """return true if the question is now published."""
        now = timezone.now()
        return now <= self.pub_date

    def can_vote(self):
        """return true if the question can be voted."""
        now = timezone.now()
        if self.end_date is None:
            return self.pub_date < now
        return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """this class create choice of the question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote(self):
        # count the votes for some_choice
        count = Vote.objects.filter(choice=some_choice).count()
        return count


class Vote(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE, null=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    @property
    def question(self):
        return self.choice.question