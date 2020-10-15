from django.shortcuts import render, get_object_or_404
from .models import Question


def index_view(request):
    questions = Question.objects.all()
    ctx = {
        'questions': questions
    }
    return render(request, 'ask.html', ctx)
