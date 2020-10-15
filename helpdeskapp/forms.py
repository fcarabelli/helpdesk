from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['subject','message','urgency']
        #fields = ['question_text', 'question_datetime']