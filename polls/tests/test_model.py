import datetime
from django.test import TestCase
from django.utils import timezone
from ..models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        future_question = Question(pub_date=timezone.localtime() + datetime.timedelta(days=30))
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        old_question = Question(pub_date=timezone.localtime() - datetime.timedelta(days=1, seconds=1))
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        recent_question = Question(pub_date=timezone.localtime() - datetime.timedelta(hours=23, minutes=59, seconds=59))
        self.assertIs(recent_question.was_published_recently(), True)

    def test_is_publish_question_with_future_pub_date(self):
        """is_published() returns False for questions whose pub_date is in the future."""
        future_question = Question(pub_date=timezone.localtime() + datetime.timedelta(days=30))
        self.assertIs(future_question.is_published(), False)

    def test_is_publish_question_with_default_pub_date(self):
        """is_published() returns True for questions whose pub_date is default."""
        default_question = Question(pub_date=timezone.localtime())
        self.assertIs(default_question.is_published(), True)

    def test_is_publish_question_with_past_pub_date(self):
        """is_published() returns True for questions whose pub_date is in the past."""
        past_question = Question(pub_date=timezone.localtime() - datetime.timedelta(days=30))
        self.assertIs(past_question.is_published(), True)
