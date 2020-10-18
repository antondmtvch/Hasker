from django import forms
from django.core.exceptions import ValidationError
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tags': forms.TextInput()
        }

    def clean_tags(self):
        tags = self.cleaned_data['tags'].split(',')
        tags = [tag.strip().lower() for tag in tags if tag.strip()]
        if len(tags) > 3:
            raise ValidationError('No more than 3 tags can be associated with the question')
        return tags
