from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Vote
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, pk):
        """To back to index page if not found"""
        self.question = get_object_or_404(Question, pk=pk)
        try:
            vote = Vote.objects.get(user=request.user,
                                    choice__in=self.question.choice_set.all())

            previous_one = vote.choice.choice_text
        except (Vote.DoesNotExist, TypeError):
            previous_one = ""

        if self.question.can_vote():
            return render(request, self.template_name, {"question": self.question,
                                                        "previous_vote": previous_one})
        else:
            messages.error(request, f"Poll number {self.question.id} is not available to vote")
            return redirect("polls:index")


class ResultsView(generic.DetailView):
    """this class display result"""
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            vote_object = Vote.objects.get(user=user)
            vote_object.choice = selected_choice
            vote_object.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, choice=selected_choice).save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def redirect_url(request):
    """redirect the url"""
    return HttpResponseRedirect(reverse('polls:index'))

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_passwd)
            login(request, user)
            return redirect('polls')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})