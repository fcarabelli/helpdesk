from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Question
        fields = ['subject','message','urgency']
        #fields = ['question_text', 'question_datetime']