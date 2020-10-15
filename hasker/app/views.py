from django.shortcuts import render
from .models import Question


def ask_view(request):
    questions = Question.objects.all()
    ctx = {
        'questions': questions
    }
    return render(request, 'ask.html', ctx)
