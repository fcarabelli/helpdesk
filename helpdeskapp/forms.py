from captcha.fields import CaptchaField
from django.forms import ModelForm,modelformset_factory
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

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        data = self.cleaned_data['email']
        # encrypt stuff
        return data

