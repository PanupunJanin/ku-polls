from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Vote
from .base import create_question


class VotingTest(TestCase):
    def setUp(self):
        """Initialize user for authenticated test"""
        self.user = User.objects.create_user(username="drago")
        self.user.set_password("m4lf0y123")
        self.user.save()
        self.client.login(username="drago", password="m4lf0y123")

    def test_vote_count(self):
        """Test vote counted correctly"""
        test_question = create_question("test_vote_count", days=-1)
        choice1 = test_question.choice_set.create(choice_text="test_choice")
        self.client.post(reverse("polls:vote", args=(test_question.id,)), {"choice": choice1.id})
        self.assertEqual(choice1.votes, 1)

    def test_unauthenticated_user_cannot_vote(self):
        """Unauthenticated vote will be redirected and authenticated user can vote"""
        self.client.logout()
        test_question = create_question("test_unauthenticated_user_cannot_vote", days=-1)
        self.assertEqual(self.client.post(reverse("polls:vote", args=(test_question.id,))).status_code,
                         302)

    def test_each_user_has_one_vote_per_question(self):
        """Each user has only one vote per question"""
        test_question = create_question("test_each_user_has_one_vote_per_question", days=-1)
        choice1 = test_question.choice_set.create(choice_text="test_choice1")
        choice2 = test_question.choice_set.create(choice_text="test_choice2")
        self.client.post(reverse("polls:vote", args=(test_question.id,)), {"choice": choice1.id})
        self.assertEqual(choice1.vote_set.get(user=self.user).choice, choice1)
        self.client.post(reverse("polls:vote", args=(test_question.id,)), {"choice": choice2.id})
        self.assertEqual(choice2.vote_set.get(user=self.user).choice, choice2)
        self.assertEqual(Vote.objects.all().count(), 1)
