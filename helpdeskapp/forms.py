from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        #fields = ['question_text', 'question_datetime']