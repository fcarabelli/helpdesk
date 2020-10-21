from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import Question




class QuestionForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Question
        fields = ['subject','message','urgency','email','phone_number']
        labels = {
            'subject': 'Asunto',
            'message': 'Mensaje',
            'urgency': 'Urgencia',
            'email': 'mail del solicitante',
            'phone_number': 'celular'
        }
        #fields = ['question_text', 'question_datetime']
        

