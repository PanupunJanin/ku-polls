from .base import create_question
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class QuestionDetailViewTests(TestCase):
    def setUp(self):
        """Set up the user before running test."""
        self.user = User.objects.create_user(username="drago")
        self.user.set_password("m4lf0y123")
        self.user.save()
        self.client.login(username="drago", password="m4lf0y123")

    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 302 Redirect Response.
        """
        future_question = create_question(question_text='Future question.', days=5)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 302)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)

    def test_past_question_unauthenticated(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text, but unauthenticated user will be redirected.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        self.client.logout()
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertEqual(response.status_code, 302)
