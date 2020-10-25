from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Question, Tag, Answer, User

QUESTION_FORM_ATTRS = {
    'class': 'form-control'
}


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=128, label='Username', widget=forms.TextInput(attrs=QUESTION_FORM_ATTRS))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=QUESTION_FORM_ATTRS))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=QUESTION_FORM_ATTRS))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=QUESTION_FORM_ATTRS))
    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=128, label='Username', widget=forms.TextInput(attrs=QUESTION_FORM_ATTRS))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=QUESTION_FORM_ATTRS))


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
