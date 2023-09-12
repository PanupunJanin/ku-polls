import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model with publish date and end date(optional)"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.localtime, blank=True)
    end_date = models.DateTimeField('date ended', null=True, blank=True)

    def __str__(self):
        """Return question text description string of each question."""
        return self.question_text

    def was_published_recently(self):
        """Return if the question is published recently(1 day)"""
        now = timezone.localtime()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Return if the question is published or not."""
        now = timezone.localtime()
        return self.pub_date <= now

    def can_vote(self):
        """Return if voting is allowed or not."""
        now = timezone.localtime()
        if self.end_date is None:
            return self.pub_date <= now
        return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """Choice model for each question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    # votes = models.IntegerField(default=0)

    @property
    def votes(self):
        """Count all the votes for this choice"""
        return self.vote_set.count()

    def __str__(self):
        """Return choice text description string of each choice."""
        return self.choice_text


class Vote(models.Model):
    """Record a choice for a question made by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} vote for {self.choice.choice_text} in {self.choice.question.question_text}"
