from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse


def index(request):
    first_few = Question.objects.all()
    context = {'first_few' : first_few, }
    return render(request, 'codes/index.html', context)

def detail(request, question_index):
    question = get_object_or_404(Question, pk = question_index)
    return render(request, 'codes/detail.html', {'question' : question})


def user_rating(request, question_index):
    question = get_object_or_404(Question, pk = question_index)
    try:
        selected_choice = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'codes/detail.html',
        {'question' : question,
        'error_message' : "You didn't select a choice.",
        })
    else:
        if selected_choice == 'YES':
            question.user_rating += 1
            question.save()
        else:
            question.user_rating -= 1
            question.save()
        return render(request, 'codes/results.html', {'question' : question})


def results(request, question_index):
    question = get_object_or_404(Question, pk=question_index)
    return render(request, 'codes/results.html', {'question': question})
