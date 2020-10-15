from django.shortcuts import render, get_object_or_404
from .models import Question


def index_view(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})


def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question.html', {'question': question})
