from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import Question




class QuestionForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Question
        fields = ['subject','message','email','phone_number']
        labels = {
            'subject': 'Asunto',
            'message': 'Mensaje',
            'email': 'mail del solicitante',
            'phone_number': 'celular'
        }
        #fields = ['question_text', 'question_datetime']
        

