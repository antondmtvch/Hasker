from django import forms
from django.core.exceptions import ValidationError

from .models import Question, Tag, Answer

QUESTION_FORM_ATTRS = {
    'class': 'form-control'
}


class CommaSeparatedTextField(forms.Field):
    widget = forms.TextInput(attrs=QUESTION_FORM_ATTRS)

    def to_python(self, value):
        tags = []
        if value:
            values = [i.lower() for i in map(str.strip, value.split(',')) if i]
            if len(values) <= 3:
                for tag_name in values:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    tags.append(tag)
                return tags
            else:
                raise ValidationError('No more than 3 tags can be associated with the question')
        return tags


class QuestionForm(forms.ModelForm):
    tags = CommaSeparatedTextField(required=False)

    class Meta:
        model = Question
        fields = ('title', 'text', 'tags')
        widgets = {
            'title': forms.TextInput(attrs=QUESTION_FORM_ATTRS),
            'text': forms.Textarea(attrs=QUESTION_FORM_ATTRS),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs=QUESTION_FORM_ATTRS)
        }
        labels = {
            'text': 'Your Answer'
        }
