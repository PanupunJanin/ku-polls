from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Choice, Question, Vote


def error_404(request, exception):
    return render(request,'polls/index.html')


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'The form is invalid')
            return redirect('signup')
        if form.is_valid():
            form.save()
            # get named fields from the form data
            username = form.cleaned_data.get('username')
            # password input field is named 'password1'
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
        return redirect('polls')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        # create a user form and display it the signup page
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class IndexView(generic.ListView):
    """Index view page of this application."""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.localtime()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detail view page of this application."""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.localtime())

    def get(self, request, *args, **kwargs):
        """Redirect user to responding pages depend on that poll's status when viewing poll's details"""
        try:
            question = get_object_or_404(Question, pk=kwargs["pk"])
        except (KeyError, Question.DoesNotExist):
            messages.error(request, 'Requested poll does not exist')
            return HttpResponseRedirect(reverse('polls:index'))
        if not question.can_vote():
            messages.error(request, 'You cannot vote on unpublished or ended poll')
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    """Results view page of this application."""
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.localtime()).order_by('-pub_date')[:5]

    def get(self, request, *args, **kwargs):
        """Redirect user to responding pages depend on that poll's status when viewing poll's results"""
        try:
            question = get_object_or_404(Question, pk=kwargs["pk"])
        except (KeyError, Question.DoesNotExist):
            messages.error(request, 'Requested poll does not exist')
            return HttpResponseRedirect(reverse('polls:index'))
        if not question.is_published():
            messages.error(request, 'This poll is not published yet')
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not question.can_vote():
        messages.error(request, "This question is not available for voting.")
        return HttpResponseRedirect(reverse('polls:index'))
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "You didn't select a choice.")
        return render(request, 'polls/detail.html', {'question': question, })
    this_user = request.user
    try:
        current_vote = Vote.objects.get(user=this_user, choice__question=question)
        current_vote.choice = selected_choice
    except Vote.DoesNotExist:
        current_vote = Vote(user=this_user, choice=selected_choice)
    current_vote.save()
    messages.success(request, "Your vote has been recorded")
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
